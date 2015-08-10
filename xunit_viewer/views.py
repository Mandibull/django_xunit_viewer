from django.shortcuts import get_object_or_404, render
import json
from lxml import etree

from .models import Project, TestResult


def index(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'xunit_viewer/index.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, 'xunit_viewer/project.html', context)


def _compute_successful(d):
    return int(d.get('tests', 0)) - int(d.get('errors', 0)) \
        - int(d.get('failures', 0)) - int(d.get('skip', 0))

def _compute_json_results(test_result, validate=True):
    schema = etree.XMLSchema(etree.parse(open('junit-4_custom.xsd'))) \
             if validate else None
    parser = etree.XMLParser(schema=schema)
    testsuite = etree.fromstring(str(test_result.xml_file), parser)
    assert(testsuite.tag == 'testsuite')
    res = {
        'stats': {
            'total_tests': int(testsuite.attrib['tests']),
            'successful': _compute_successful(testsuite.attrib),
            'errors': int(testsuite.attrib['errors']),
            'failures': int(testsuite.attrib['failures']),
            'skipped': int(testsuite.attrib['skip']),
        },
        'tests': [],
    }

    for testcase in testsuite:
        assert(testcase.tag == 'testcase')
        _res = {
            'class_name': testcase.attrib['classname'],
            'name': testcase.attrib['name'],
            'time': testcase.attrib['time'],
            'result': 'success',
        }
        for node in testcase:
            if node.tag in ('error', 'failure'):
                _res['result'] = node.tag
                _res['error_type'] = node.attrib['type']
                _res['error_message'] = node.attrib['message']
                _res['error_data'] = node.text
            elif node.tag in ('system-out', 'system-err'):
                _res['error_message'] = node.text  # FIXME: not error_message!!!
            res['tests'].append(_res)

    test_result.json_results = json.dumps(res)
    test_result.save()
    return res


def test_result(request, test_result_id):
    test_result = get_object_or_404(TestResult, pk=test_result_id)
    # if test_result.json_results is None or not test_result.json_results:
    json = _compute_json_results(test_result)
    context = {'test_result': test_result,
               'results': json}
    return render(request, 'xunit_viewer/test_result.html', context)

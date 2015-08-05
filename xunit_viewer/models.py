from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    xunit_output_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TestResult(models.Model):
    project = models.ForeignKey(Project)
    xml_file = models.TextField()
    json_results = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.project.name, self.date)

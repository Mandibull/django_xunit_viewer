from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_id>[0-9]+)/$', views.project, name='project'),
    url(r'^test/(?P<test_result_id>[0-9]+)/$', views.test_result, name='test_result'),
]

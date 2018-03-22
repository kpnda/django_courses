from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/process/$', views.add_course_process),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^destroy/process/$', views.delete_course_process),
]
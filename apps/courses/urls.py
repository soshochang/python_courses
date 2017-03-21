from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^add_course$', views.add_course),
  url(r'^remove/(?P<id>\d+)$', views.remove_course),
  url(r'^remove_page/(?P<id>\d+)$', views.remove_course_page),
  # url(r'^result$', views.result)
]
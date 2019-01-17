from django.conf.urls import url
from django.urls import re_path
from labels import views

__author__ = 'minjoon'


urlpatterns = [
    re_path(r'^create/(?P<slug>\d+)/$', views.LabelCreateView.as_view(), name='labels-create'),
    re_path(r'^list/(?P<query>[\w+]+)/$', views.LabelListView.as_view(), name='labels-list'),
    re_path(r'^download/(?P<query>[\w+]+)/$', views.LabelDownloadView.as_view(), name='labels-download'),
    re_path(r'^delete/(?P<slug>\d+)/$', views.LabelDeleteView.as_view(), name='labels-delete'),
    re_path(r'^detail/(?P<slug>\d+)/$', views.LabelDetailView.as_view(), name='labels-detail'),
]

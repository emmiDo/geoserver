'''
Created on Jul 21, 2014

@author: minjoon
'''

from django.conf.urls import url
from django.urls import re_path
from questions import views

urlpatterns = [
    re_path(r'^upload/$', views.QuestionUploadView.as_view(), name='questions-upload'),
    re_path(r'^upload/choice$', views.ChoiceUploadView.as_view(), name='questions-upload-choice'),
    re_path(r'^list/(?P<query>[\w+]+)/$', views.QuestionListView.as_view(), name='questions-list'),
    re_path(r'^delete/(?P<slug>\d+)/$', views.QuestionDeleteView.as_view(), name='questions-delete'),
    re_path(r'^download/(?P<query>[\w+]+)/$', views.QuestionDownloadView.as_view(), name='questions-download'),
    re_path(r'^update/all/$', views.QuestionUpdateAllView.as_view(), name='questions-update_all'),
    re_path(r'^update/(?P<slug>\d+)/$', views.QuestionUpdateView.as_view(), name='questions-update'),
    re_path(r'^detail/(?P<slug>\d+)/$', views.QuestionDetailView.as_view(), name='questions-detail'),
    re_path(r'^createtag/$', views.TagCreateView.as_view(), name='questions-tagcreate'),
]
from django.conf.urls import url
from django.urls import re_path
from semantics import views

__author__ = 'minjoon'


urlpatterns = [
                       re_path(r'^annotate/(?P<question_pk>\d+)/(?P<sentence_index>\d+)/$', views.SentenceParseAnnotateView.as_view(), name='semantics-annotate'),
                       re_path(r'^download/(?P<query>[\w+]+)/$', views.SemanticParseDownloadView.as_view(), name='semantics-download'),
                       re_path(r'^list/(?P<query>[\w+]+)/$', views.SemanticParseListView.as_view(), name='semantics-list'),
                       re_path(r'^annotate/(?P<question_pk>\d+)/(?P<choice_number>\d+)/$', views.ChoiceAnnotateView.as_view(), name='semantics-choice-annotate'),
                       # url(r'^detail/(?P<slug>\d+)/$', views.LabelDetailView.as_view(), name='labels-detail'),
]

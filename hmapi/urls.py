from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^books/$', views.BookList.as_view(), name="books"),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name="books"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
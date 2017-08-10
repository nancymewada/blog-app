from django.conf.urls import url,include
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^post/new/$',post_new, name='post_new'),
    url(r'^/$',post_list,name='post_list'),
    url(r'^posts/(?P<pk>\d)/$',post_detail,name="post_detail"),
]

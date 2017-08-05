#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^index/', views.MainPageView.as_view(), name='index'),
    url(r'^login/$', views.acc_login, name='login'),
    url(r'^register/$', views.acc_registerView.as_view(), name='register')
]

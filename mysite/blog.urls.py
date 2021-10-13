# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:11:07 2021

@author: Виктория
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

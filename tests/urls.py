# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('django_url_toolkit.urls', namespace='django_url_toolkit')),
]

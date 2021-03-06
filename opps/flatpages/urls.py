#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import PageDetail


urlpatterns = patterns(
    '',

    # FLATPAGEs
    url(r'^(?P<slug>[\w]+)$',
        cache_page(60 * 2)(PageDetail.as_view()), name='open'),
)

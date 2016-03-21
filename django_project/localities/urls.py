# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import (
    LocalitiesLayer,
    LocalityInfo,
    DataLoaderView
)

urlpatterns = patterns(
    '',
    url(
        r'^localities.json$', LocalitiesLayer.as_view(),
        name='localities'
    ),
    url(
        r'^localities/(?P<uuid>\w{32})$', LocalityInfo.as_view(),
        name='locality-info'
    ),
    url(
        r'^localities/(?P<uuid>\w{32})/(?P<changes>[0-9].*)$', LocalityInfo.as_view(),
        name='locality-info-history'
    ),
    url(
        r'^localities/edit$', 'localities.views.locality_edit_view',
        name='locality-edit'
    ),
    url(
        r'^localities/create$', 'localities.views.locality_create_view',
        name='locality-create'
    ),

    url(
        r'^search/localities/name$',
        'localities.views.search_locality_by_name',
        name='locality-name-search'
    ),

    url(
        r'^countries$',
        'localities.views.search_countries',
        name='countries'
    ),

    url(
        r'^search/localities/country$',
        'localities.views.search_locality_by_country',
        name='locality-country-search'
    ),

    url(
        r'^locality/updates$',
        'localities.views.get_locality_update',
        name='locality-updates'
    ),

    url(
        r'^upload-form$', DataLoaderView.as_view(), name='upload-form'
    ),
    url(
        r'^load-data$', 'localities.views.load_data', name='load-data'
    ),

    # url(r'^search$', SearchView.as_view(), name='search')
)

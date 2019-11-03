from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('mail/', send_online, name='send_online_url'),

    path('products/', products_list, name='products_list'),
    path('product/create/', ProdCreate.as_view(), name='product_create_url'),
    path('product/<str:slug>/', product_detail, name='product_detail_url'),
    path('product/<str:slug>/update', ProdUpdate.as_view(), name='product_update_url'),

    path('services/', services_list, name='services_list'),
    path('service/create/', ServiceCreate.as_view(), name='service_create_url'),
    path('services/<str:slug>/', service_detail, name='service_detail_url'),
    path('services/<str:slug>/update', ServiceUpdate.as_view(), name='service_update_url'),

    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('portfolio/create/', PortfolioCreate.as_view(), name='portfolio_create_url'),
    path('portfolio/<str:slug>/', portfolio_detail, name='portfolio_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
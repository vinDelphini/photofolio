from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('gallery-single/', views.gallery_single, name='gallery-single'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('sample-inner-page/', views.sample_inner_page, name='sample-inner-page'),
    path('ero/', views.ero, name='ero'),

    # gallery
    path('nature/', views.nature, name='nature'),
]
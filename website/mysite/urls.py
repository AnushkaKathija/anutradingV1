from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('products', views.products, name='products'),
    path('mechanical', views.mechanical, name='mechanical'),
    path('fibreoptics', views.fibreoptics, name='fibreoptics'),
    path('abrasivematerials', views.abrasivematerials, name='abrasivematerials'),
    path('electricals', views.electricals, name='electricals'),
    path('instrumentation', views.instrumentation, name='instrumentation'),
    path('telecommunication', views.telecommunication, name='telecommunication'),
    path('brands', views.brands, name='brands')
]

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='index.html'), name='about'),
    path('products/', TemplateView.as_view(template_name='index.html'), name='products'),
    path('products/phones/', TemplateView.as_view(template_name='index.html'), name='phones'),
    path('products/laptops/', TemplateView.as_view(template_name='index.html'), name='laptops'),
    path('products/phones/apple/', TemplateView.as_view(template_name='index.html'), name='apple_phones'),
    path('products/phones/samsung/', TemplateView.as_view(template_name='index.html'), name='samsung_phones'),
    path('products/laptops/apple/', TemplateView.as_view(template_name='index.html'), name='apple'),
    path('products/laptops/lenovo/', TemplateView.as_view(template_name='index.html'), name='lenovo_laptops'),
    ]
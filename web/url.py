from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='web/index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='web/about.html'), name='about'),
    path('our-services/', TemplateView.as_view(template_name='web/services.html'), name='services'),
    path('contact/', TemplateView.as_view(template_name='web/contact.html'), name='contact'),
    path('track/', TemplateView.as_view(template_name='web/index.html'), name='track'),
    path('news/', TemplateView.as_view(template_name='web/news.html'), name='news'),

]

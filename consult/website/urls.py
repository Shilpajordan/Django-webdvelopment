from django.urls import path
from . import views
from .views import webhook_handler

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('webhook/', webhook_handler, name='webhook_handler'),
]
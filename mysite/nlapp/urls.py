from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter')
]
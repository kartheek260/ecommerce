from django.urls import path
from homeapp import views
from django.conf.urls import include
app_name='homeapp'

urlpatterns = [
   path('', views.home),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('front', views.front,name='front')
]
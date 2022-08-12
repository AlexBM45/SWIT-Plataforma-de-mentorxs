from django.urls import path
from mentor import views

urlpatterns = [
    path('', views.index, name = 'name')
]
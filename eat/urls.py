from django.urls import path

from . import views

app_name = 'eat'
urlpatterns = [
    path('', views.index, name='eat'),
]
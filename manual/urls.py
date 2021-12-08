from django.urls import path

from . import views

app_name = 'manual'
urlpatterns = [
    path('', views.index, name='manual'),
]
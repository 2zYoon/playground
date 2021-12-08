from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('log-out/', views.logout, name='logout'),
]
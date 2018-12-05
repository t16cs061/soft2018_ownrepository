from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/logged_out', auth_views.LogoutView.as_view(), name='logout'),
]
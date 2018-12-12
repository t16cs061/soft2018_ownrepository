from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('mentenance', views.mentenance, name='mentenance'),
    path('mentereserve', views.mentenance_reserve, name='mentereserve'),
    path('mentecheck', views.mentenance_check, name='mentecheck'),
    path('registration/logged_out', auth_views.LogoutView.as_view(), name='logout'),
    path('admin', admin.site.urls),
]
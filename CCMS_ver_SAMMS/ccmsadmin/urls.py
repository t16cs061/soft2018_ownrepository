from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='adminindex'),
    path('adminadd', views.add, name='adminadd'),
    path('admindelete/<int:num>',views.delete,name='admindelete'),
    path('adminedit/<int:num>', views.edit, name='adminedit'),
    path('registration/logged_out', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('shopping_list', views.shopping_list),
    path('toggle_item', views.toggle_item),
    path('remove_item', views.remove_item),
    path('remove_list', views.remove_list),
    path('add_item', views.add_item),
    path('add_list', views.add_list),
    path('login', auth_views.LoginView.as_view()),
    path('logout', auth_views.LogoutView.as_view()),
    path('register', views.register)
]
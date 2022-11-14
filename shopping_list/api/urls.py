from django.urls import path

from . import views


urlpatterns = [
    path('get_shopping_lists', views.get_shopping_lists)
]
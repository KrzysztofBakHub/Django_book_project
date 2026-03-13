from django.urls import path

from . import views


urlpatterns = [
    path('', views.welcome),
    path('book_search/', views.book_search)]

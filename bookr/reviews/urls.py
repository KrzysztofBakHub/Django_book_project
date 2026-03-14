from django.urls import path

from . import views


urlpatterns = [
    path('', views.welcome),
    path('books/', views.book_list, name='book_list'),]

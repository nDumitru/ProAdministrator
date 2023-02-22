from django.urls import path

from intro import views

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_books/', views.books, name='list-of-books')
]
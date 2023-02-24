from django.urls import path

from management import views

urlpatterns = [
    path('create_administrator/', views.AdministratorCreateView.as_view(), name='create-administrator'),
    path('list_of_administrators/', views.AdministratorListView.as_view(), name='list-of-tadministrators'),
    path('update_administrator/<int:pk>/', views.AdministratorUpdateView.as_view(), name='update-administrator'),
    path('delete_administrator/<int:pk>/', views.AdministratorDeleteView.as_view(), name='delete-administrator'),
    path('details_of_administrator/<int:pk>/', views.AdministratorDetailView.as_view(), name='details-of-administrator'),
    path('inactive_administrator/<int:pk>/', views.inactivate_Administrator, name='inactive-administrator')

]

from django.urls import path

from residents import views

urlpatterns = [
    path('create_resident/', views.ResidentCreateView.as_view(), name='create-residents'),
    path('list_of_residents/', views.ResidentListView.as_view(), name='list-of-residents'),
    path('update_resident/<int:pk>/', views.ResidentUpdateView.as_view(), name='update-residents'),
    path('delete_resident/<int:pk>/', views.ResidentDeleteView.as_view(), name='delete-residents'),
    path('details_of_resident/<int:pk>/', views.ResidentDetailView.as_view(), name='details-of-residents'),
    path('inactive_resident/<int:pk>/', views.inactivate_resident, name='inactive-residents'),

]

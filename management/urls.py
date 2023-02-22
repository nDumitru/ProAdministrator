from django.urls import path

from management import views

urlpatterns = [
    path('create_tariner/', views.TrainerCreateView.as_view(), name='create-management'),
    path('list_of_tariners/', views.TrainerListView.as_view(), name='list-of-trainers'),
    path('update_trainers/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-management'),
    path('delete_trainers/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-management'),
    path('details_of_traines/<int:pk>/', views.TrainerDetailView.as_view(), name='details-of-management'),
    path('inactive_trainer/<int:pk>/', views.inactivate_trainer, name='inactive-management')

]

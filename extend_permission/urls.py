from django.urls import path
from .views import (
    ExtendPermissionListView,
    ExtendPermissionCreateView,
    ExtendPermissionUpdateView,
    ExtendPermissionDeleteView
)

app_name = 'extend_permission'

urlpatterns = [
    path('', ExtendPermissionListView.as_view(), name='extend_permission_list'),
    path('create/', ExtendPermissionCreateView.as_view(), name='extend_permission_create'),
    path('<int:pk>/update/', ExtendPermissionUpdateView.as_view(), name='extend_permission_update'),
    path('<int:pk>/delete/', ExtendPermissionDeleteView.as_view(), name='extend_permission_delete'),
]

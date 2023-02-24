from django.urls import path
from residents import views
from .views import ResidentListView

app_name = 'residents'

urlpatterns = [
    path('', views.index, name='index'),
    path('', ResidentListView.as_view(), name='resident-list'),
    path('resident/<int:pk>/', views.ResidentDetailView.as_view(), name='resident_detail'),
    path('resident/add/', views.ResidentCreateView.as_view(), name='resident_add'),
    path('resident/<int:pk>/update/', views.ResidentUpdateView.as_view(), name='resident_update'),
    path('resident/<int:pk>/delete/', views.ResidentDeleteView.as_view(), name='resident_delete'),
]

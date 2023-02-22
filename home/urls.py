from django.urls import path

from home import views
from home.views import HomeTemplateView
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('search/', views.search, name='search'),
]

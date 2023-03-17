from django.urls import path
from main import views

urlpatterns = [
    path('dream/', views.dream_list),
    path('dream/<id>', views.dream_detail)
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('update/<str:pk>/', views.update, name="updatepage"),
    path('delete/<str:pk>/', views.delete, name="deletepage")
]


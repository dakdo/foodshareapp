from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.ListPost.as_view()),
    path('posts/<int:pk>/', views.DetailPost.as_view()),
]
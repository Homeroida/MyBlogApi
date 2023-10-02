from django.urls import path
from .views import PostListCreateView, PostDetailView, CategoryListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('category/', CategoryListCreateView.as_view()),

]

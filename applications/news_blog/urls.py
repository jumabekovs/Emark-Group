from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
]
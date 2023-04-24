from django.urls import path
from .views import FlatListView, FlatDetailView

urlpatterns = [
    path('flat/list/', FlatListView.as_view()),
    path('flat/<int:pk>/', FlatDetailView.as_view()),
]
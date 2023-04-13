from django.urls import path
from .views import ConstructionListView, ConstructionDetailView, FlatListView, FlatDetailView

urlpatterns = [
    path('list/', ConstructionListView.as_view()),
    path('<int:pk>/', ConstructionDetailView.as_view()),
    path('flat/list/', FlatListView.as_view()),
    path('flat/<int:pk>/', FlatDetailView.as_view()),
]
from django.urls import path
from .views import DocumentListView, DocumentDetailView

urlpatterns = [
    path('list/', DocumentListView.as_view()),
    path('<int:pk>/', DocumentDetailView.as_view()),
]

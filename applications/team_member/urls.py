from django.urls import path
from .views import MemberListView, MemberDetailView


urlpatterns = [
    path('list/', MemberListView.as_view()),
    path('<int:pk>/', MemberDetailView.as_view()),
]
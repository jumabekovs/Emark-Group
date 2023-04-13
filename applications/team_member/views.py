from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Member
from .serializers import MemberListSerializer, MemberDetailSerializer


class MemberListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer


class MemberDetailView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Member, Partner
from .serializers import MemberListSerializer, MemberDetailSerializer, PartnerSerializer
from .filters import MemeberFilter


class MemberListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MemeberFilter


class MemberDetailView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer


class PartnerView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

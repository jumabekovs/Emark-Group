from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Construction, Flat, Block
from .serializers import ConstructionListSerializer, ConstructionDetailSerializer, \
    FlatListSerializer, FlatDetailSerializer, BlockSerializer
from .filters import ConstructionFilter, FlatFilter


class ConstructionListView(ListAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ConstructionFilter
    lookup_field = 'selling_status'
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'completed_objects_count': Construction.objects.filter(selling_status='в продаже').count(),
            'selling_objects_count': Construction.objects.filter(selling_status='построено').count()
        }
        return response


class ConstructionDetailView(RetrieveAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionDetailSerializer


class FlatListView(ListAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlatFilter

    def get_queryset(self):
        return super().get_queryset().filter(
            construction_id=self.kwargs['pk']
        )


class FlatDetailView(RetrieveAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatDetailSerializer


class BlockView(ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

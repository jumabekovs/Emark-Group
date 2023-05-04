from rest_framework.generics import ListAPIView
from .models import History
from .serializers import HistorySerializers


class HistoryListView(ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

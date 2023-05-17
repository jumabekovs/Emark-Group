from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Document
from .serializers import DocumentSerializer


class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer



class DocumentDetailView(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

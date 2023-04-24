from rest_framework import viewsets
from .models import Configuration
from .serializers import ConfigurationSerializer


class ConfigurationView(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_serializer_context(self):
        return {'request': self.request}

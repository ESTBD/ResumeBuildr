from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 

from .models import RequestModel
from .serializers import HTMLDataSerializer

class HTMLtoPDFView(viewsets.ModelViewSet):

    queryset = RequestModel.objects.all()
    serializer_class = HTMLDataSerializer 

    def create(self, request, *args, **kwargs):
        return Response({"message": "Recieved html!"})
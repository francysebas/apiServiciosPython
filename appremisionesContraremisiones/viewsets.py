from rest_framework import viewsets
from .models import Remision_Contraremision, Acompanante
from .serializer import RemisionSerializer, AcompananteSerializer

class RemisionViewSet(viewsets.ModelViewSet):
    queryset = Remision_Contraremision.objects.all()
    serializer_class = RemisionSerializer


class AcompananteViewSet(viewsets.ModelViewSet):
    queryset = Acompanante.objects.all()
    serializer_class = AcompananteSerializer

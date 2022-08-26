from airport_app.models import *
from airport_app.serializers import *
from rest_framework import viewsets, status
# Create your views here.
# aqui va la logica y los url

class Avion_view(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = Avion_Serializer

class Piloto_view(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = Piloto_Serializer



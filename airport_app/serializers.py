#from django.contrib.gis.gdal.raster import source
from rest_framework import serializers
from airport_app.models import *

class Avion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = '__all__'

class Piloto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'
class Tripulacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tripulacion
        fields = '__all__'

class Vuelo_serializer(serializers.ModelSerializer):
    avion = Avion_Serializer(read_only=True) #get
    avion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Avion.objects.all(),source='avion') #post
    piloto = Piloto_Serializer(read_only=True) #get
    piloto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Piloto.objects.all(),source='piloto') #post

    class Meta:
        model = Vuelo
        fields = '__all__'

class Itinerario_serializer(serializers.ModelSerializer):
    vuelo = Vuelo_serializer(read_only=True) #get
    vuelo_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vuelo.objects.all(),source='vuelo') #post
    tripulacion = Tripulacion_Serializer(read_only=True) #get
    tripulacion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset='tripulacion') #post
    class Meta:
        model = Itinerario
        fields = '__all__'


from django.db.models import fields
from rest_framework import serializers
from .models import *

class PddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdd
        fields = '__all__'

class RecToSq(serializers.ModelSerializer):
    class Meta:
        model = RecToSq
        fields = '__all__'       

class Tar(serializers.ModelSerializer):
    class Meta:
        model = Tar
        fields = '__all__'          

class TarToPdd(serializers.ModelSerializer):
    class Meta:
        model = TarToPdd
        fields = '__all__' 

class SsdToSsd(serializers.ModelSerializer):
    class Meta:
        model = SsdToSsd
        fields = '__all__'         

class MuSsd(serializers.ModelSerializer):
    class Meta:
        model = MuSsdTechnique
        fields = '__all__'   

class MuSadTechnique(serializers.ModelSerializer):
    class Meta:
        model = MuSadTechnique
        fields = '__all__'  

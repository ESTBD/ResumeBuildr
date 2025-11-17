from rest_framework import serializers 
from .models import RequestModel

class HTMLDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ['htmldata']


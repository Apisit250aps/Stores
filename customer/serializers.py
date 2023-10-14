from rest_framework import serializers

from . import models

class CustomerDataSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = models.CustomerData
        fields = "__all__"


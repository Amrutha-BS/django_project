from rest_framework import serializers
from .models import Destination,contact_Us

class DestinationSerializer(serializers.ModelSerializer):
      class Meta:
        model =Destination
        fields = ('id', 'name', 'img', 'desc','date','price','seller_fname','seller_lname','email')
class contact_UsSerializer(serializers.ModelSerializer):
      class Meta:
        model = contact_Us
        fields = ('id', 'first_name', 'last_name','email','msg','date')
    
from rest_framework import serializers
from .models import Tables, Computers



class ComputersSerializer(serializers.ModelSerializer):
  class Meta:
    model = Computers
    fields = '__all__'


class TableSerializer(serializers.ModelSerializer):

    computer_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tables
        fields = '__all__'
    
    def get_computer_details(self, obj):   
        computer_details = obj.computers_set.all()
        serializer = ComputersSerializer(computer_details, many=True)
        return serializer.data
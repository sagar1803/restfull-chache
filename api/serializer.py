from django.db.models import fields
from rest_framework import serializers
from . models import Books

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = '__all__' #To return all fields
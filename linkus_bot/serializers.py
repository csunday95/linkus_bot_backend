from rest_framework import serializers
from .models import *


class UserDisciplineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDisciplineType
        fields = '__all__'


class UserDisciplineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDisciplineEvent
        fields = '__all__'

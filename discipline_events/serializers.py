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
        read_only_fields = [
            'discipline_start_date_time',
            'id'
        ]
        depth = 2


class CreateUserDisciplineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDisciplineEvent
        fields = '__all__'

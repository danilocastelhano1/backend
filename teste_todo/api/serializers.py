from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import TODO

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ['id', 'conteudo', 'is_completo']


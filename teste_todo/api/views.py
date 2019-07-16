from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TODOSerializer
from .models import TODO
from rest_framework.response import Response

class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer




from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CodecompaniontestSerializer
from .models import Codecompaniontest

# Create your views here.

class CodecompaniontestView(viewsets.ModelViewSet):
    serializer_class = CodecompaniontestSerializer
    queryset = Codecompaniontest.objects.all()
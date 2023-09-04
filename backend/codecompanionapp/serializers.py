from rest_framework import serializers
from .models import Codecompaniontest

class CodecompaniontestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codecompaniontest
        fields = ('id', 'title', 'description', 'completed')
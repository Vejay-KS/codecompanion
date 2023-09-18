from rest_framework import serializers
from .models import Codecompaniontest, CodeCompanionUser

class CodecompaniontestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codecompaniontest
        fields = ('id', 'title', 'description', 'completed')

class CodeCompanionUserrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeCompanionUser
        fields = ('id', 'username', 'password1', 'password2', 'email', 'role', 'firstmname', 'lastname')
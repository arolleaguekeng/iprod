from rest_framework import serializers

from api.models import User,Creation

from api.base_64_converter import Base64ImageField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = '__all__'
        image = Base64ImageField()




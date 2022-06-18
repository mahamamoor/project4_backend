from rest_framework import serializers
from .models import Account
from django.contrib.auth.hashers import make_password, check_password


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'password')

    
    def create(self, validated_data):
        user = Account.objects.create(
        name=validated_data['name'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

 
    def update(self,instance, validated_data):
        user = Account.objects.get(name=validated_data["name"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user
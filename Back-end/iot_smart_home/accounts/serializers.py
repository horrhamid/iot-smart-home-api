from rest_framework import serializers
from .models import User, Customer, Contractor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'address', 'gender', 'age', 'role', 'first_name', 'last_name',
                  'email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Customer
        fields = ('user',)


class ContractorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Contractor
        fields = ('user', 'under_service_area', 'salary', 'resume')


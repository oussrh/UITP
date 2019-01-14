from rest_framework import serializers

from . import models

Choix = [tuple([x,x]) for x in range(0,5)]


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    # class Meta:
    #     model = models.UserProfile
    #     fields = ['name']
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'last_login', 'password')
        extra_kwargs = {
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Used to create a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incidents
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Detail
        fields = '__all__'

class RapportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rapports
        fields = '__all__'

class TransportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transports
        fields = '__all__'


class TypeIncidentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.TypeIncidents
        fields = '__all__'
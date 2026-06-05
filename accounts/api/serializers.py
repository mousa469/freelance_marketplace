from rest_framework import serializers
from django.contrib.auth.models import User
from .. models import Profile




class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    role = serializers.CharField()



    def validate_username(self, value ):
        if User.objects.filter(username = value ).exists():
            raise serializers.ValidationError("Username already exist")
        return value
    
    def validate_role(self, value):
        if value not in [Profile.CLIENT_ROLE , Profile.FREELANCER_ROLE]:
            raise serializers.ValidationError("Role must be client or freelancer")
        return value

    

    def create (self , validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create_user(username=username ,password=password )
        user.profile.role = validated_data["role"]
        user.profile.save()
        return user



    



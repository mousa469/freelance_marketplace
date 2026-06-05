from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

class RegisterAPIView(APIView):
    def post(self , request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
           token =  Token.objects.create(user = user)
           return Response({"token": token.key} , status.HTTP_201_CREATED )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

            
        
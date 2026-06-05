from django.urls import path
from rest_framework.authtoken.views  import obtain_auth_token
from . import views



urlpatterns=[
    path('login' , obtain_auth_token ),
    path('register' , views.RegisterAPIView.as_view() )

]
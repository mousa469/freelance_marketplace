from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    CLIENT_ROLE = "client"
    FREELANCER_ROLE = "freelancer"


    Role_CHOICES=[
        (FREELANCER_ROLE , "Freelancer"),
        ( CLIENT_ROLE , "Client")
    ]
    user = models.OneToOneField(User , on_delete=models.CASCADE ,related_name="profile")
    role = models.CharField(max_length= 10 ,choices=Role_CHOICES, null=True ,blank=False)
    bio = models.CharField(max_length=200 ,blank=True)
    skills = models.CharField(max_length=100 , blank=True)
    hourly_rate = models.DecimalField(max_digits=10 , decimal_places=2 , blank=True , null=True)
    portfolio = models.URLField(max_length=300 , blank=True)


    def __str__(self):
        return f"{self.user.username}"
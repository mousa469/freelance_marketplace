

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(sender=User , signal= post_save )
def create_user_profile(sender , instance , created , *args,**kwargs):
    if created:
        Profile.objects.create(user = instance)


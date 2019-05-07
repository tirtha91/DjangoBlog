# To create profile automatically after a users SignUp or a object is saved
# User model is the sender of the signal
# Create a receiver which gets this signal from sender and performs a task
# When a user is saved User model sends a signal and this signal is received by create_profile along with the 'instance'=user
# **kwargs means it will accept any additional argument
from django.db.models.signals import post_save
from django.contrib.auth.models import User   
from django.dispatch import receiver
from .models import Profile

@receiver(post_save , sender=User)
def create_profile(sender , instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save , sender=User)
def save_profile(sender , instance, **kwargs):
    instance.profile.save()
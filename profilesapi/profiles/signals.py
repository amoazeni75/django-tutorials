from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


# every time an user created, the following function would be called automatically
# and create an user_profile instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)

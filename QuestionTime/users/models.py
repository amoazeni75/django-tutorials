from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    # here you can add any custom fields to the user model
    pass

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver



# Create your models here.
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    description = models.CharField(max_length=500, blank=True)
    profile_picture = CloudinaryField('image')

    def __str__(self):
        return f"{self.user.username} \'s Profile"

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

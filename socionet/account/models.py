from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Profile model extends the user profile """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        """string representation of model object"""
        return f'Profile for user {self.user.username}'
    
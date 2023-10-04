from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #We add CASCADE here because. If the user is deleted. Their Profile is also deleted.
    image = models.ImageField(default='default.jpg',upload_to='profile_pictures')

    def __str__(self):
        return f"{self.user.username} Profile"
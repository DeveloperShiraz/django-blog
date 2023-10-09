from django.db import models #This imports post model from models.
from django.utils import timezone #This imports timezone from Django Utilities.
from django.urls import reverse
from django.contrib.auth.models import User #This imports User from Django Auth Models.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
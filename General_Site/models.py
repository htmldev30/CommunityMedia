from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=100, null=True)
    user_image_icon = models.FileField(upload_to="user_profile_icons")
        
    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Communities(models.Model):
    user_created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="User")
    community_name = models.CharField(max_length=25, null=True)
    community_bio  = models.CharField(max_length=100,null=True)
    community_image_icon = models.FileField(upload_to="community_icons", null=True, 
                                            default='/community_icons/default_community_icon.jpg')
    community_created_time = models.DateTimeField(auto_now_add=True)
    community_slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Communities"

    def __str__(self):
        return self.community_name

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    community_slug = slugify(instance.community_name)
    exists = Communities.objects.filter(community_slug=community_slug).exists()
    if exists:
        community_slug = "%s_%s" %(community_slug, instance.id)

    instance.community_slug = community_slug


pre_save.connect(pre_save_post_receiver, sender=Communities)

# Simple Posting Page
class Posts(models.Model):
    user_posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="User_Posted_By")
    community = models.ForeignKey(Communities, on_delete=models.CASCADE, null=True)

    post_content = models.CharField(max_length=180, null=True)
    post_pic = models.FileField(upload_to="post_pics", default="", blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.post_content
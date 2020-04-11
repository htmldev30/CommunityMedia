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

    post_header = models.CharField(max_length=50, null=True)
    post_content = models.CharField(max_length=180, null=True)
    post_pic = models.FileField(upload_to="post_pics", default="", blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)
    post_slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.post_content

def pre_save_post_receiver_post(sender, instance, *args, **kwargs):
    post_slug = slugify(instance.post_header)
    exists_post = Posts.objects.filter(post_slug=post_slug).exists()
    if exists_post:
        post_slug = "%s_%s" % (post_slug, instance.id)

    instance.post_slug = post_slug

pre_save.connect(pre_save_post_receiver_post, sender=Posts)


# Commenting On Post
class Comments(models.Model):
    post = models.ForeignKey(Posts, null=True, on_delete=models.CASCADE, related_name="Comment")
    user_commented_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.CharField(max_length=180, null=True)
    comment_pic = models.FileField(upload_to="post_pics/comment_pics", default="", blank=True)
    time_commented = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return 'Comment by {}'.format(self.user_commented_by)


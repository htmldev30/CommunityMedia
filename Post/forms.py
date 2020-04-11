from django.forms import ModelForm
from .models import Posts, Communities, Comments


class CommunityForm(ModelForm):
	class Meta:
		model = Communities
		fields = ["community_name", "community_bio", "community_image_icon"]


class PostForm(ModelForm):
	class Meta:
		model = Posts
		fields = ["post_header","post_content", "post_pic", "community"]


class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ["comment", "comment_pic"]

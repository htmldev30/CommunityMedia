from django.shortcuts import render, HttpResponse
from Post.models import Communities # Communities List For Dropdown
from .models import UserProfile
from Post.forms import PostForm, CommunityForm
from django.contrib.auth.models import User
# Create your views here.


def home(request, pk=None):


	# User Profile 
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user


	# Handling POSTS SUBMISSIONS

	if User.is_authenticated:
		if request.method == "POST":
			post_form = PostForm(request.POST, request.FILES)
			if post_form.is_valid():
				post_instance = post_form.save(commit=False)
				post_instance.user_posted_by = request.user
				post_instance.save()

		else:

			post_form = PostForm()


	# Communitites
	communities = Communities.objects.all()

	if User.is_authenticated:
		community_form = CommunityForm(request.POST)
		if request.method == "POST":
			community_form = CommunityForm(request.POST, request.FILES)
			if community_form.is_valid():
				community_post_instance = community_form.save(commit=False)
				community_post_instance.user_created_by = request.user
				community_post_instance.save()
		else:
			community_post_instance = CommunityForm()

	# Users 

	all_users = UserProfile.objects.all()

	context = {"user" : user, "communities" : communities, "all_users" : all_users, "post_form" : post_form, "community_form" : community_form}
	return render(request, "Views_Templates/dashboard.html", context)




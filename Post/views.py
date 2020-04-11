from django.shortcuts import render, redirect, get_object_or_404
from .models import Communities, Posts, Comments
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
# Create your views here.

def communities(request):
    communities = Communities.objects.all()
    context = {"communities" : communities}
    return render(request,"communities_page.html", context)


def community_page(request, c_slug):
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

    community = get_object_or_404(Communities, community_slug=c_slug)
    posts = Posts.objects.filter(community=community)


    context = {"community": community, "posts": posts, "post_form": post_form}

    return render(request, "community.html", context)

def post_iso(request, c_slug, p_slug):
	community = get_object_or_404(Communities, community_slug=c_slug)
	post_iso = Posts.objects.get(post_slug=p_slug)
	if request.method=="POST": 
		comment_form = CommentForm(request.POST, request.FILES)
		if comment_form.is_valid():
			comment_instance = comment_form.save(commit=False)
			comment_instance.post = post_iso
			comment_instance.user_commented_by = request.user
  
			comment_instance.save()
	else:
		comment_form = CommentForm()

	comments = Comments.objects.filter(post=post_iso).order_by('-time_commented') # Getting the Comment Object.Post and assinging it to a specific post with slug
	context = {"comment_form" : comment_form, "post_iso" : post_iso, "comments" : comments}
	return render(request, "post_iso.html", context)
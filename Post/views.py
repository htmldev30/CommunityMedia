from django.shortcuts import render, redirect, get_object_or_404
from .models import Communities, Posts
from django.contrib.auth.models import User
# Create your views here.

def communities(request):
    communities = Communities.objects.all()
    context = {"communities" : communities}
    return render(request,"communities_page.html", context)



def post(request):
	# Will be a simple page to post features will include the community they want to post to
	return ""


def community_page(request, slug):


	community = get_object_or_404(Communities, community_slug=slug)

	posts = Posts.objects.filter(community=community)

	context = {"community" : community, "posts" : posts}
	return render(request, "community.html", context)



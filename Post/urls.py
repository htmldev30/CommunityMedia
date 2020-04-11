from django.urls import path
from . import views
urlpatterns = [
    path("c/", views.communities,name="communities"),
    path("c/<slug>/", views.community_page, name="community_page"),
    path("post/", views.post, name="post"), # Add posting feature to dashboard page also
]
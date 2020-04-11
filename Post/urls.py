from django.urls import path
from . import views
urlpatterns = [
	path("c/", views.communities, name="communities"),
    path("c/<slug:c_slug>/", views.community_page, name="community_page"),
    path("c/<slug:c_slug>/<slug:p_slug>/", views.post_iso, name="post_iso"), # Add posting feature to dashboard page also
]
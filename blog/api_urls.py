from django.urls import path
from rest_framework.authtoken import views
from blog.api_views import post_list, post_detail
from django.urls import path
from django.urls import include

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>/", post_detail, name="api_post_detail"),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token)
]
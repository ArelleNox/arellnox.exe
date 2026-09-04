from django.urls import path
from . import views

urlpatterns = [ path("", views.home, name="home"), 
                path("posts/<str:group>/<str:lang>/", views.post_detail, name="post_detail"),]
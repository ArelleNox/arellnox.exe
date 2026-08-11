from django.shortcuts import render

from .models import Post 
def home(request): 
    lang = request.GET.get("lang", "en") 
    posts = Post.objects.filter(language=lang, is_published=True) 
    context = { "posts": posts, "current_lang": lang, } 
    return render(request, "blog/home.html", context) 
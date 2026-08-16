from django.shortcuts import render, get_object_or_404
from .models import Post 

UI_TEXT = { "en": { "brand": "Arellnox.exe", "eyebrow": "a personal, no-niche blog", "hero_title": "Thoughts kept<br>at <em>quiet</em> hours", "hero_desc": "<strong>No niche, no schedule</strong> — just the things I'm learning, playing, cooking and coding.", "btn_read": "Read the journal →", "shelves_h2": "What lives here", "posts_h2": "Recent entries", "footer": "Arellnox — a slow blog, updated when there's something worth saying", }, 
            "fr": { "brand": "Arellnox.exe", "eyebrow": "un blog personnel, sans thème unique", "hero_title": "Pensées gardées<br>à l'heure <em>calme</em>", "hero_desc": "<strong>Pas de thème, pas d'horaire</strong> — juste ce que j'apprends, joue, cuisine et code.", "btn_read": "Lire le journal →", "shelves_h2": "Ce qu'on trouve ici", "posts_h2": "Derniers articles", "footer": "Arellnox — un blog lent, mis à jour quand il y a quelque chose à dire", }, 
            "ja": { "brand": "アレルノックス.exe", "eyebrow": "テーマのない個人ブログ", "hero_title": "静かな時間に<br>綴った<em>想い</em>", "hero_desc": "<strong>テーマもスケジュールもなく</strong>—学んでいること、遊んでいること、料理やコーディングのことなど。", "btn_read": "ジャーナルを読む →", "shelves_h2": "ここにあるもの", "posts_h2": "最近の記事", "footer": "アレルノックス — 書くことがあるときに更新する、ゆっくりしたブログ", }, }

def home(request): 
    lang = request.GET.get("lang", "en") 
    posts = Post.objects.filter(language=lang, is_published=True) 
    context = { "posts": posts, "current_lang": lang, "ui": UI_TEXT.get(lang, UI_TEXT["en"]), }
    return render(request, "blog/home.html", context)
 
def post_detail(request, slug): 
    post = get_object_or_404(Post, slug=slug, is_published=True) 
    context = { "post": post, "ui": UI_TEXT.get(post.language, UI_TEXT["en"]), } 
    return render(request, "blog/post_detail.html", context)
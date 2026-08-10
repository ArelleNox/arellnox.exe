from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("fr", "Français"),
        ("ja", "日本語"),
    ]

    CATEGORY_CHOICES = [
        ("games", "Video Games"),
        ("gamedev", "Game Development"),
        ("books", "Books"),
        ("growth", "Personal Growth"),
        ("cooking", "Cooking"),
        ("random", "Everything & Anything"),
    ]

    # Shared across every language-version of the "same" post.
    # e.g. all three (EN/FR/JA) versions of "comfort games" share
    # translation_group = "comfort-games". This is what lets the
    # site know they're translations of each other.
    translation_group = models.SlugField(
        max_length=100,
        help_text="Same value across all language versions of one post, e.g. 'comfort-games'."
    )

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)  # auto-filled from title, see save() below
    excerpt = models.CharField(max_length=300)
    content = models.TextField()

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # A given (translation_group, language) pair should only exist once —
        # you can't have two English versions of "comfort-games".
        unique_together = ("translation_group", "language")
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.language}] {self.title}"
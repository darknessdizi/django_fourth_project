from django.contrib import admin
from .models import Article, Tags, TagsArticle


class RelationshipInline(admin.TabularInline):
    model = TagsArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(TagsArticle)
class TagsArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag', 'is_main']

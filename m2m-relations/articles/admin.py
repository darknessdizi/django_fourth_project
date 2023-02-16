from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


# @admin.register(Tags)
# class TagsAdmin(admin.ModelAdmin):
#     # list_display = ['id', 'name']
#     pass


# @admin.register(ArticleTags)
# class ArticleTagsAdmin(admin.ModelAdmin):
#     # list_display = ['id', 'article', 'tags', 'is_main']
#     pass



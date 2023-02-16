from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=30)
    arcticles = models.ManyToManyField(Article, through='TagsArticle', related_name='scopes')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class TagsArticle(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Связь m2m'
        verbose_name_plural = 'Связи m2m'
    
    # def __str__(self):
    #     return self.name
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().prefetch_related('scopes')
    print(object_list)
    print('*'*40)
    for i in object_list:
        print(i.title, i.text)
        for y in i.scopes.all():
            print('+'*10, y)
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)

from django.shortcuts import render

from .models import Article


def articles_list(request):
    ordering = '-published_at'
    template = 'articles/news.html'
    articles = Article.objects.all().order_by(ordering)
    context = {'object_list': articles}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)

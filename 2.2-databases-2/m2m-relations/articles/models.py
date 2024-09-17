from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    tags = models.ManyToManyField(Tag, through='scope', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_scopes(self):
        scopes = self.scopes.all()
        main = scopes.filter(is_main=True).first()

        if main:
            sorted_scopes = [main] + list(scopes.exclude(id=main.id).order_by('tag__name'))

        return sorted_scopes


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

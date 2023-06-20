import datetime

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='заголовок')
    blog_slug = models.CharField(max_length=100, verbose_name='slug')
    blog_content = models.TextField(verbose_name='содержимое', **NULLABLE)
    blog_preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    blog_created_at = models.DateField(verbose_name='создан', default=datetime.date.today)
    blog_is_publicated = models.BooleanField(verbose_name='опубликован', default=False)
    blog_views_count = models.BigIntegerField(verbose_name='количество просмотров', default=0)

    def inc_view_count(self):
        self.blog_views_count += 1
        return self.blog_views_count

    def save(self, *args, **kwargs):  # new
        if not self.blog_slug:
            self.blog_slug = slugify(self.blog_title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.blog_title}\nСоздан: {self.blog_created_at}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('blog_title',)


from django.db import models

# Create your models here.
class yldam_news(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовки')
    content = models.TextField(blank=True,verbose_name='Текст')
    photo = models.ImageField(upload_to='news_photos/%Y/%m/%d/',verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время обновления')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering= ['-time_create','title']


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name
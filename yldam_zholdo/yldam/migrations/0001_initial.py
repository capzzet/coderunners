# Generated by Django 4.2.1 on 2023-05-06 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yldam_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовки')),
                ('content', models.TextField(blank=True, verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='news_photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]

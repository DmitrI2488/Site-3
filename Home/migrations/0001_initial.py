# Generated by Django 4.0.3 on 2022-04-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название канала')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('url', models.URLField(verbose_name='Ссылка на канал')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата публикации')),
                ('rating', models.IntegerField(blank=True, null=True, verbose_name='Рейтинг')),
                ('passed', models.BooleanField(verbose_name='Прошел ли проверку?')),
            ],
        ),
    ]
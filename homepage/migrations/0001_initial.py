# Generated by Django 3.2.6 on 2022-12-17 05:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='氏名')),
                ('furigana', models.CharField(max_length=255, verbose_name='ふりがな')),
                ('picture', models.CharField(max_length=255, verbose_name='写真')),
                ('text', models.TextField(verbose_name='メッセージ')),
                ('stars', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], verbose_name='星の数')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='氏名')),
                ('furigana', models.CharField(max_length=255, verbose_name='ふりがな')),
                ('picture', models.CharField(max_length=255, verbose_name='写真')),
                ('text', models.TextField(verbose_name='メッセージ')),
                ('stars', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], verbose_name='星の数')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]
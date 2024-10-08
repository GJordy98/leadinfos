# Generated by Django 5.0.3 on 2024-04-04 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('auteur', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(0, 'DRAFT'), (1, 'PUBLISHED')], default=0, max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post-images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='articles.category')),
            ],
        ),
    ]

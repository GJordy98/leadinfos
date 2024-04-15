from django.db import models
from django.contrib.auth.models import User

import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
STATUS = ((0,'DRAFT'), (1,'PUBLISHED'))

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    titre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    auteur = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    contenu = models.TextField(default="Contenu")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='post-images/', blank=True, null=True)

    def __str__(self):
        return self.titre
    

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

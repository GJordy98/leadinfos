from django.contrib import admin
from .models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'slug', 'status', 'category', 'created')
    list_filter = ('status', 'category')
    search_fields = ('titre', 'content')

admin.site.register(Post,PostAdmin)

admin.site.register(Category)
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles'),
    path('search/', views.search_view, name='search'),
    path('creer/', views.create_view, name='create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='details'),
    
    ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
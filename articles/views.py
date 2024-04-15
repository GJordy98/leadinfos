from django.shortcuts import redirect, render
from django.views import generic
from .views import generic
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'articles/articles.html'
    paginate_by = 2


class PostDetail(generic.DeleteView):
    model = Post
    template_name = 'articles/details.html'


def create_view(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        form.save()
        return redirect('articles')
    return render(request, 'articles/creer.html', context={'form': form})


def search_view(request):
    search = request.GET.get('search')
    posts =  Post.objects.filter(Q(titre__contains=search) )

    posts_number = posts.count()
    message = f'{posts_number} resultats'

    if posts_number == 1:
        message = f'{posts_number} resultat'

    context = {'posts':posts,
               'message': message}

    
    return render(request, 'articles/search.html', context)
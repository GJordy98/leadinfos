from django.shortcuts import get_object_or_404, render
from .forms import contactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from articles.models import Category
from articles.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home_view(request, category=None):
    Posts = Post.objects.all()
    Categories = Category.objects.all()
    pposts2 = Post.objects.all()[:3]
    categories2 = Category.objects.all()[:5]

    if category:
        category = get_object_or_404(Category, slug=category)
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page':page,
        'Categories': Categories,
        'pposts2': pposts2,
        'categories2': categories2,
    }
    return render(request, 'accueil.html', context)

def contact_view(request):
    form = contactForm()
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            titre = f'| {nom} {prenom} {email}'
            send_mail(titre, message, 'glennjordy1998@gmail.com', ['glennjordy1998@gmail.com', 'glennjordy1997@gmail.com'])
            return HttpResponseRedirect(reverse('merci'))
    return render(request, 'contact.html', context={'form': form})


def merci_view(request):
    return render(request,'merci.html')

def propos_view(request):
    return render(request, 'propos.html')
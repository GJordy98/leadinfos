from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def inscription_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth_app/inscription.html', context={'form':form})



def connect_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou Mot de passe incorrect")
    return render(request, 'auth_app/connexion.html')


def deconnexion_view(request):
    logout(request)
    return redirect('connexion')
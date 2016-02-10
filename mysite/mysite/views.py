from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.utils import timezone
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm, InscriptionForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def ConnexionView(request):
    error = False
    
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    
    return render(request, 'connexion.html', locals())

def InscriptionView(request):
    error = False
    
    if request.method == "POST":
        form = IscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["pseudo"]
            name = form.cleaned_data["prenom"]
            lastname = form.cleaned_data["nom"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            passwordconf = form.cleaned_data["passwordconf"]
            if password != passwordconf:
                error = True
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name, user.last_name = name, lastname
                if user:
                    login(request, user)
                else:
                    error = True
        else:
            error = True
    else:
        form = InscriptionForm()

    return render(request,'inscription.html', locals())

def ProfilView(request):
    
    return render(request,'profil.html')

def deconnexion(request):
    logout(request)
    return redirect(reverse(ConnexionView))
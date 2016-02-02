from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone


# Create your views here.

def ConnexionView(request):
	
	return render(request,'connexion.html')

def InscriptionView(request):
    
    return render(request,'inscription.html')

def ProfilView(request):
    
    return render(request,'profil.html')

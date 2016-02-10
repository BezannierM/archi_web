from django import forms
from django.contrib.auth import authenticate,login

class ConnexionForm(forms.Form):
    username = forms.CharField(label="", max_length=30)
    password = forms.CharField(label="", widget=forms.PasswordInput)

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label="", max_length=30)
    prenom = forms.CharField(label="", max_length=30)
    nom = forms.CharField(label="", max_length=30)
    email = forms.CharField(label="", max_length=30)
    password = forms.CharField(label="", widget=forms.PasswordInput)
    passwordconf = forms.CharField(label="", widget=forms.PasswordInput)
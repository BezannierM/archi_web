import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Evenement(models.Model):
    nom = models.CharField(max_length=100)
    date_eve = models.DateField(default=True)
    nb_personne = models.PositiveIntegerField(default=0)
    createur = models.ForeignKey(User, id)
    participant = User.objects.all()

class Profil(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return "{0}".format(self.user.username)
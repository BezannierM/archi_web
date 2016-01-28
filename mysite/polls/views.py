from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone


from .models import User, Evenement



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_user_list'

    def get_queryset(self):
        return User.objects.order_by('username')

class DetailView(generic.DetailView):
    model = User
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = User
    template_name = 'polls/results.html'




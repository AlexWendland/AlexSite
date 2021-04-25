from django.shortcuts import render
from django.views import generic

from .models import *

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'papers'
    
    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')


class TalksView(generic.ListView):
    template_name = "talks_index.html"
    context_object_name = 'talks'
    
    def get_queryset(self):
        return Talk.objects.order_by('-date_given')

class TalkDetailView(generic.DetailView):
    model = Talk
    template_name = 'talk.html'

class TeachingView(generic.ListView):
    template_name = "teaching.html"
    context_object_name = 'teaching'
    
    def get_queryset(self):
        return Teaching.objects.order_by('-start_date')

class AwardsView(generic.ListView):
    template_name = "awards.html"
    context_object_name = 'awards'
    
    def get_queryset(self):
        return Award.objects.order_by('-date_obt')
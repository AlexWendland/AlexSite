from django.shortcuts import render
from django.views import generic

from .models import Paper

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = 'papers'
    
    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')



from .models import Post
from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'txt2htm/post_detail.html'

class PostCreateView(generic.edit.CreateView):
    model = Post
    fields = ['body']
    def get_success_url(self):
        return reverse('txt2htm:detail',
                       args=[self.object.pk])

def convert(request, iden):
    body = get_object_or_404(Body, pk=iden)
    return HttpResponseRedirect(reverse('txt2htm:create', args=(iden.id,)))
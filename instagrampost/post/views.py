from django.shortcuts import render
from post.models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.


class CreatePost(CreateView):
    model = Post
    fields = ['username','caption']
    success_url = reverse_lazy('postlist_page')

class showPost(ListView):
    model = Post
    template_name = 'post/postlist.html'
    context_object_name = 'postlist'
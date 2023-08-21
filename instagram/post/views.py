from django.shortcuts import render,HttpResponse
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


def remove_post(request,post_id=0):
    if post_id:
        try:
            post = Post.objects.get(id =post_id)
            post.delete()
            return HttpResponse("post deleted sucessfully")
        except:
            
            return HttpResponse("Please Enter a valid Emp id")
    post = Post.objects.get(id = post_id)
    context = {
        'post':post
    }
    return render(request,'delete.html',context)
    
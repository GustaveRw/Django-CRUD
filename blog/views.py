from django.shortcuts import render
from blog.models import Post
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = “__all__”
    success_url

class PostDetailView(DetailView):
    model = Post

    class PostUpdateView(UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

    class PostDeleteView(UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

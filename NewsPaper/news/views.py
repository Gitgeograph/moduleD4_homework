from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .filters import PostFilter
from .forms import PostForm
from .models import Post

class PostList(ListView):
    model = Post
    ordering = ['-creationData']
    template_name = 'post/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
    

class PostSearch(ListView):
    model = Post
    ordering = ['-creationData']
    template_name = 'post/post_search.html'
    context_object_name = 'post_search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset = self.get_queryset())
        context['form'] = PostForm()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
       id = self.kwargs.get('pk')
       return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post/post_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('news:all_posts')


class HomeView(TemplateView):
    template_name = 'post/home_page.html'
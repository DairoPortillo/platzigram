from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from posts.forms import PostForm
from posts.models import Post


"""
@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})
"""


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

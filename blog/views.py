from django.shortcuts import render, get_object_or_404
from .models import Post, Blogger, Commenter, Comment
import datetime
# Create your views here.
def index(request):
    """View function for blog homepage"""
    auth_counts = Blogger.objects.all().count()
    post_counts = Post.objects.all().count()
    best_blog = Comment.objects.all()
    a = dict()
    for i in best_blog:
        if a.get(i.post) == None:
            a[i.post] = 1
        else:
            a[i.post] += 1
    n, t = '',  0
    for i, j in a.items():
        if j > t:
            n, t = i, j
    best_blog = n
    num = t
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context  = {
        'index_title': 'Welcome Home',
        'auth_counts': auth_counts,
        'post_counts': post_counts,
        'best_blog': best_blog,
        'num': num,
        'num_visits': num_visits,
        'my_github': 'https://github.com/Jay-davisphem',
        'author': 'David Oluwafemi',
    }
    return render(request, 'index.html', context=context)

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5

class BloggerDetailView(generic.DetailView):
    model = Blogger

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class CommentCreate(LoginRequiredMixin, CreateView, Commenter):
    model = Comment
    fields = ['comment',]
    template_name = 'blog/comment_form.html'
    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.post = get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'],})

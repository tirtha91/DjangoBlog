from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myblogApp.models import Post

# Create your views here
def Home(request):
    context = {
        # Creating a dictionary and in the value part passing the above dictionary
        # passing the post from DB to the HTML
        'blogPosts' : Post.objects.all()
    }
    # context pass the data from view to the template and the key 'blogPosts' will be accessible within template
    return render(request , 'myblogApp/home.html' , context)

# view for the lists of posts or home page
class PostListView(ListView):
    # Declare a variable 'model' that tells which model to query for creating Posts
    model = Post
    # appname/model_viewtype.html is the default template where it will search for
    template_name = "myblogApp/home.html"          
    context_object_name = 'blogPosts' 
    ordering = ['-date_posted']  
    paginate_by = 5

class UserPostListView(ListView):
    # Declare a variable 'model' that tells which model to query for creating Posts
    model = Post
    # appname/model_viewtype.html is the default template where it will search for
    template_name = "myblogApp/user_posts.html"          
    context_object_name = 'blogPosts'  
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# view for the post details
class PostDetailView(DetailView):
    model = Post  
    # template_name = "myblogApp/post_detail.html"  not reqd as we have given the default naming format
    
# view for creating post,it returns a form and we just need to add the fields
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title' , 'content']
    # template_name = "myblogapp/post_form" as it shares the same for with update post also

    def form_valid(self, form):
        # the current logged in user has been set as the author of the form and 
        # it is overriding the form_valid moethod before returning 
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title' , 'content']
    # template_name = "myblogapp/post_form" as it shares the same for with update post also

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # template = it will use the form of create post only

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # view for deleting post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def About(request):
    return render(request , 'myblogApp/about.html' , { 'title' : 'About us'})




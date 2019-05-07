from django.urls import path
from . import views
from .views import PostListView , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView

urlpatterns = [
    # 1-keep the path as blank to make it as Homepage 
    # 2-mention which view.fucntion will be displayed here
    # 3- name helps to understand that this views.Home method is from this myblogApp
    # We cannot give class name directly but need to convert it to as_view()
    # for post/<int:pk>/ we are using dynamic URL so that it takes the pri key of the post that is to be viewed
    path('', PostListView.as_view() , name='myblogApp-home'), 
    path('user/<str:username>', UserPostListView.as_view() , name='user-posts'), 
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),   
    path('about/', views.About , name='myblogApp-About'),
]

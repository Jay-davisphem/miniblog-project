from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.PostListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger'),
    path('blog/<int:pk>/comment/', views.CommentCreate.as_view(), name='add_comment'),
    path('blog/create', views.BlogCreate.as_view(), name='blog_create'),
]

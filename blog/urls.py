from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, toggle_published

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('published/<int:pk>/', toggle_published, name='toggle_published'),

]

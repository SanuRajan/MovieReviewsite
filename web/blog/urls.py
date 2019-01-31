from django.urls import path
from django_filters.views import FilterView
from blog import views

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    MovieUpdateView,
    PostDeleteView,
    PostCommCreateView,
    

)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('post/<int:pk>/other/',PostCommCreateView.as_view(), name='post-other-update'), #view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/search', views.search, name = 'search'),
]

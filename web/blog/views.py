from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

from .models import Movie
from .models import Comm


 
class PostListView(ListView):  #List all the movies
	model = Movie
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Movie


def get_context_data(self, **kwargs):     # showing all comments and rating of all users to a movie
       context = super().get_context_data(**kwargs)
       form = CommUpdateForm()
       context.update({'form': form})
       return context


	

class PostCreateView(LoginRequiredMixin, CreateView): #Creates a New Movie
	model = Movie
	fields = ['title','ratings','my_genre','my_image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def about(request):
		return render (request,'blog/home.html')

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #updates the movie of the user
	model = Movie
	fields = ['title','ratings','my_genre','my_image']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		return True

class PostCommCreateView( CreateView):
	model =  Comm
	fields = ['ratings', 'comments']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		return True



class PostSearchView():
	model = Movie


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Movie
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def search(request):
  query = request.GET.get('q')
  posts = Movie.objects.filter(Q(title__icontains=query)|Q(my_genre__icontains=query))
  return render(request, 'blog/search.html', {'posts': posts})


def about(request):
	return render (request,'blog/about.html')




import django_filters

from blog.models import  Movie


class FilmFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	genre = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Movie
		fields = ['title', 'my_genre']
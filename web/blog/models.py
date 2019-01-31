from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image



list_of_genre = [

    ('Horror', 'Horror'),
    ('Sci-fi', 'Sci-fi'),
    ('Thriller', 'Thriller'),
    ('Action', 'Action')
    
]

class Movie(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.FloatField(null = True, validators=[MaxValueValidator(10), MinValueValidator(1)] )
    my_genre = models.TextField(max_length= 100,null= True,choices=list_of_genre)
    my_image = models.ImageField(default='', upload_to='movie_pics')
    

    def __str__(self):
        return f'{self.title}Movie'

    def save(self , *args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.my_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.my_image.path) 
   
    def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title


class Comm(models.Model):
    movie = models.ManyToManyField(Movie)
    name = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    ratings = models.FloatField(null = True, validators=[MaxValueValidator(10), MinValueValidator(1)] )
    comments= models.CharField(max_length=100)


    def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.comments




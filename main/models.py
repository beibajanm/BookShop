from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=85,blank=True)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True,null=True,upload_to='authors')

class Genre(models.Model):
    slug = models.SlugField(max_length=55,primary_key=True)
    name = models.CharField(max_length=55,unique=True)

class Book(models.Model):
    CHOICES = (
        ('in stock','В наличии'),
        ('out of stock','Нет в наличии')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True,null=True,upload_to='books')
    status = models.CharField(choices=CHOICES,max_length=20)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
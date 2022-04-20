from django.db import models

class Author(models.Model):
	name = models.CharField('Author Name', max_length=50)

class Book(models.Model):
	name = models.CharField('Book A', max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
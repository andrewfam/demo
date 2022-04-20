from django.shortcuts import render

from .models import *

# Create your views here.
def load_books(request):
	books = Book.objects.all()

	template = 'load_books.html'
	template_vars = { 'books': books}
	return render(request, template, template_vars)

def load_exceptions(request):
	numbera = 10/ 1
	number = 10 / 0

	template = 'load_exceptions.html'
	template_vars = {}
	return render(request, template, template_vars)
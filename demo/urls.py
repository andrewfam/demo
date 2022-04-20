from django.urls import path

from . import views

urlpatterns = [
	path('all/', views.load_books, name='load-books'),
	path('exceptions/', views.load_exceptions, name='load-exceptions'),   
]
from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .GoogleBooksService import ControllerGetInfoBook

def home(request):
    return render(request, 'home.html')

def search(request):
    name=request.POST.get('bookname')
    return name
      
def response_search(request):
    booksearch= search(request)
    book=ControllerGetInfoBook.created_book(f'{booksearch}')
    return render(request,'search.html',{'book':book})





from django.shortcuts import render, redirect  
from django.http import HttpResponse
from decouple import config
import requests


class MyTolken:

    MYAPIKEY= config('KEY')
    
class GetBook(MyTolken):

    @classmethod
    def get_book(cls,search):     
        url=f'https://www.googleapis.com/books/v1/volumes?q={search}&key={cls.MYAPIKEY}'
                            
        response=requests.get(url= url)
        print(search)
        #print(response.status_code)
        response_json=response.json()
        itens=response_json['items']
        return itens

class Book:

    def __init__(self, title, authors, publishedDate, description, thumbnail, textSnippet):
        self.title=title
        self.authors=authors
        self.publishedDate=publishedDate
        self.description=description
        self.thumbnail=thumbnail
        self.textSnippet=textSnippet

class ControllerGetInfoBook:


    @classmethod
    def created_book(cls, search):
        content=GetBook.get_book(search)
        book_list=list()

        for book in content:

            info=book['volumeInfo']
            title=info.get('title')
            authors=info.get('authors')
            publishedDate=info.get('publishedDate')
            description=info.get('description')
            image=info.get('imageLinks')
            searchInfo=book.get('searchInfo')

            if authors is None:
                author='dont exist this information'
            else:
                author=authors[0]
            if image is None:
                thumbnail='dont exist this information'
            else:
                thumbnail=image.get('smallThumbnail')
            if searchInfo is None:
                textSnippet='dont exist this information'
            else:
                textSnippet=searchInfo.get('textSnippet')
            if description is None: 
                description='dont exist this information'
            
            book=Book(title, author, publishedDate, description, thumbnail, textSnippet)
            book_list.append(book)

        return book_list

    

def home(request):
    return render(request, 'home.html')

def search(request):
    name=request.POST.get('bookname')
    return name
      
def response_search(request):
    booksearch= search(request)
    book=ControllerGetInfoBook.created_book(f'{booksearch}')
    return render(request,'search.html',{'book':book})





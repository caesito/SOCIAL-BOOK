from decouple import config
import requests

class MyTolken:

    MYAPIKEY= config('KEYBOOKS')
    
class GetBook(MyTolken):

    @classmethod
    def get_book(cls,search):     
        url=f'https://www.googleapis.com/books/v1/volumes?q={search}&key={cls.MYAPIKEY}'
                            
        response=requests.get(url= url)
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
            nofound='-'

            if authors is None:
                author=nofound
            else:
                author=authors[0]
            if image is None:
                thumbnail=nofound
            else:
                thumbnail=image.get('smallThumbnail')
            if searchInfo is None:
                textSnippet=nofound
            else:
                textSnippet=searchInfo.get('textSnippet')
            if description is None: 
                description=nofound
            
            book=Book(title, author, publishedDate, description, thumbnail, textSnippet)
            book_list.append(book)

        return book_list
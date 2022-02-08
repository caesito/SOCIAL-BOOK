from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('search', views.response_search, name= 'search')
]


# Book Directory Test README

This read me will guide you through the program 

### Setup

pull the code and run the command

```Python
pip install -r requiremnets.txt
```

Created the models, serializers and most important views.py 

### Views.py

```Python
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genres = self.request.query_params.get('genre')
        
        if genres is not None:
            genre_list = genres.split(',')
            queryset = queryset.filter(genres__genre__in = genre_list)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'
```
These 2 view classes re generic classes of rest framework and they display values according to the url search query sent.

### settings.py > pagination settings

```Python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination PageNumberPagination',
    'PAGE_SIZE': 10
}
```

The page_size of 10 will display 10 objects at a time

### book_app.urls.py

```Python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('<str:name>/', views.BookDetailView.as_view()),
]
```

### Sending URLs

```
1. http://localhost:8000/?name="<book_name>"

2. http://localhost:8000/?genre="<genre(s)>" (seperated by a comma)
```
1. Returns a single book with the name 
2. Returns the list of books with the genre(s) searched by
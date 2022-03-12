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
            print(genre_list)
            queryset = queryset.filter(genres__genre__in = genre_list)
            print(set(queryset))
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'
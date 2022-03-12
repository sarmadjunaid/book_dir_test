from cgitb import lookup
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        print(genre)
        if genre is not None:
            queryset = queryset.filter(genre = genre)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'
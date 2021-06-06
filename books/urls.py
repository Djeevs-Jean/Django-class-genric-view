from django.urls import path
from .views import IndexView, BookDetailView, CreateBookView, UpadteBookView, DeleteBookView

# app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='book_list'),
    # path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/created/', CreateBookView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', UpadteBookView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', DeleteBookView.as_view(), name='book_delete'),

]

from django.urls import path
from .views import IndexView, BookDetailView, CreateBookView, UpadteBookView, DeleteBookView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('create-view/', CreateBookView.as_view(), name='bookcreate-view'),
    path('update-view/<int:pk>/', UpadteBookView.as_view(), name='bookupdate-view'),
    path('delete-view/<int:pk>/', DeleteBookView.as_view(), name='bookdelete-view'),

]

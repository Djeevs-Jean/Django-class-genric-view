from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.views.generic import ListView
from books.models import Books
from django.db.models import F
from django.utils import timezone
from .forms import BookForm


class IndexView(ListView):

    model = Books
    template_name = 'book-list.html'
    context_object_name = 'books'
    paginate_by = 5  # Pagination over-write
    # queryset = Books.objects.all()[:2]
    # queryset = Books.objects.filter(title='')

    #Alturnative override class methods.
    #def get_queryset(self):
        #return Books.objects.all()[:3]

    #Alturnative override class methods.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        return context


# class GenreView(ListView):
#     model = Books
#     template_name = 'book-list.html'
#     context_object_name = 'books'
#     paginate_by = 2  # Pagination over-write

#     def get_queryset(self, *args, **kwargs):
#         return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # post = Books.objects.filter(slug=self.kwargs.get('slug'))

        context['time'] = timezone.now()
        return context

class CreateBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'bookcreate-view.html'
    success_url = reverse_lazy('books:bookcreate-view')

class UpadteBookView(UpdateView):
    model = Books
    template_name = 'bookupdate-view.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('books:bookupdate-view')


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'bookdelete-view.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('books:bookdelete-view')



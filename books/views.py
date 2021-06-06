from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.views.generic import ListView
from .models import Books
from django.db.models import F
from django.utils import timezone
from .forms import BookForm

# from django.urls import reverse, redirect
from django.shortcuts import render, get_object_or_404, redirect, reverse




class IndexView(ListView):

    model = Books
    template_name = 'book_list.html'
    # context_object_name = 'books'
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
    template_name = 'book_detail.html'
    # context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # post = Books.objects.filter(slug=self.kwargs.get('slug'))

        context['time'] = timezone.now()
        return context

class CreateBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_create.html'
    # success_url = reverse_lazy('books:bookcreate-view')

    # def form_valid(self, form_class):
    #     # form_class.instance.author = get_author(self.request.user)
    #     form_class.save()
    #     return redirect(reverse("book_detail", kwargs={
    #         'pk': form_class.instance.pk
    #     }))

class UpadteBookView(UpdateView):
    model = Books
    template_name = 'book_update.html'
    fields = '__all__'
    # pk_url_kwarg = 'pk'
    # success_url = reverse_lazy('books:bookupdate-view')


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'book_delete.html'
    fields = '__all__'
    # pk_url_kwarg = 'pk'
    # success_url = reverse_lazy('books:bookdelete-view')



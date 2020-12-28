from django import forms
from .models import Books


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('title', 'author', 'post')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            # 'post': forms.TextInput(widgets = {
            'post': forms.Textarea(attrs={'cols': 40, 'rows': 6, 'class': 'form-control'}),
        }

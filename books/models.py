from django.db import models

from django.urls import reverse

class Books(models.Model):
    # Example model only
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    post = models.TextField(max_length=250, blank=True)
    # genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # isbn = models.CharField(max_length=100)
    # count = models.IntegerField(null=True, default=0)

    # class Meta:
    #     ordering = ('-list_date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("book_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("book_delete", kwargs={"pk": self.pk})
    
    
    
    

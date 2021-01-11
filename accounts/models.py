from django.db import models

# Create your models here.


class Book(models.Model):
    email = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='books/image/', null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.email

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)

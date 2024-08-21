from django.db import models
from django.utils import timezone as time

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100, unique=True, blank=False, default="")
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=time.now)
    updated_at = models.DateTimeField(default=time.now)
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return self.title

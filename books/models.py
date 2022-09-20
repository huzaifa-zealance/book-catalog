from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.CharField(max_length=255)
    avg_rating = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "books"

    def __str__(self):
        return self.name
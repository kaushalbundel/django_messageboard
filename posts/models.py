from django.db import models
from django.urls import reverse


# Create your models here.

class Posts(models.Model):
    title = models.TextField(default="Random title value as a default")
    description = models.TextField(default="Random Value for defaults sake.")
    post_date = models.DateTimeField(default="2024-06-10 12:00:00")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

from django.db import models

# Create your models here.
class Books(models.Model):
    bookId = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.bookId

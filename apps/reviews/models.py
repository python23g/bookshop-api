from django.db import models
from django.contrib.auth.models import User
from apps.books.models import Book


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, help_text="Enter a rating between 1 and 5")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.book.title}"

    class Meta:
        ordering = ['-timestamp']

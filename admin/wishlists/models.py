from django.db import models
from django.utils import timezone


class Wishlists(models.Model):
    book_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now, editable=False)

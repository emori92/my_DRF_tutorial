import uuid
from datetime import timedelta
# django
from django.db import models


class Book(models.Model):

    class Meta:
        db_table = 'book'
    
    def __str__(self):
        return self.title

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length = 20)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

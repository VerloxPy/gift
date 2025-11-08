from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=200, verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
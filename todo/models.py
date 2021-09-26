from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=now, editable=False)
    iscompleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

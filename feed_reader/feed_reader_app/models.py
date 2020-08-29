from django.db import models

# Create your models here.
class Item(models.Model):

   title = models.TextField()
   summary = models.TextField()
   link = models.TextField()
   published = models.DateTimeField()

   class Meta:
      db_table = "items"

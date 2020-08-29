from django.db import models


class Category(models.Model):

   name = models.TextField()

   def __str__(self):
       return self.name

   class Meta:
      db_table = "categories"


# Create your models here.
class Item(models.Model):

   title = models.TextField()
   summary = models.TextField()
   link = models.TextField()
   published = models.DateTimeField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

   class Meta:
      db_table = "items"

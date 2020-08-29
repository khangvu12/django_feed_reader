from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'   # Name for the list as a template variable
    template_name = 'feed_reader_app/item_list_template.html'  # Specify the template name/location

    def get_queryset(self):
        return Item.objects.all() # Get items

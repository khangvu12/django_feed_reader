from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item

class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'   # Name for the list as a template variable
    template_name = 'feed_reader_app/item_list_template.html'  # Specify the template name/location
    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

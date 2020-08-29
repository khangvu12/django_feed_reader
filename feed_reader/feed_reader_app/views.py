from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Item
import django_filters
from django_filters import IsoDateTimeFilter


class ItemFilterset(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['category']


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        # Use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context


class ItemListView(FilteredListView):
    filterset_class = ItemFilterset
    model = Item
    context_object_name = 'item_list'   # Name for the list as a template variable
    template_name = 'feed_reader_app/item_list_template.html'  # Specify the template name/location
    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

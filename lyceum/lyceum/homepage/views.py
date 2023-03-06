from django.shortcuts import render

from catalog.models import Item

# from django.http import HttpResponse


# Create your views here.
def home(request):
    template = "homepage/index.html"
    items = Item.objects.published().filter(is_on_main=True)
    context = {
        "items": items,
    }
    return render(request, template, context)

import django.shortcuts
from django.http import HttpResponse
from django.shortcuts import render

import catalog.models


# Create your views here.
def item_list(request):
    template = "catalog/item_list.html"
    items = django.shortcuts.get_list_or_404(
        catalog.models.Item.objects.published().order_by(
            "category__name", "name"
        ),
    )
    context = {
        "items": items,
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = "catalog/view_element.html"
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.published().order_by(
            "category__name", "name"
        ),
        pk=pk,
    )
    context = {
        "item": item,
    }
    return render(request, template, context)


def item_data_detail(request, dt, pk):
    if pk <= 0:
        return HttpResponse(status=404)
    return HttpResponse("<body>Подробно элемент</body>")

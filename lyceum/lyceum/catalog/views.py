from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def item_list(request):
    template = "catalog/item_list.html"
    context = {}
    return render(request, template, context)


def item_detail(request, pk):
    template = "catalog/view_element.html"
    context = {}
    return render(request, template, context)


def item_data_detail(request, dt, pk):
    if pk <= 0:
        return HttpResponse(status=404)
    return HttpResponse("<body>Подробно элемент</body>")

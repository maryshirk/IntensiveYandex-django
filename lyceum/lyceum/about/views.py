from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here.
def description(request):
    template = "about/about.html"
    context = {}
    return render(request, template, context)

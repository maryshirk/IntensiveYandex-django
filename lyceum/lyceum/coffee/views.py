from django.http import HttpResponse


def index(request):
    return HttpResponse("<body>Я чайник</body>", status=418)

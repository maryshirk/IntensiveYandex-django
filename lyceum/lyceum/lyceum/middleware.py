from django.http import HttpResponse

from lyceum.settings import REVERSE_FLAG


class SimpleMiddleware:
    c = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.c += 1
        response = self.get_response(request)
        if self.c % 10 == 0:
            r = response.content.decode()
            if REVERSE_FLAG:
                if response.status_code == 200 or response.status_code == 418:
                    s = "<body>" + r[6:-7][::-1] + "</body>"
                    response = HttpResponse(s, status=200)
        return response

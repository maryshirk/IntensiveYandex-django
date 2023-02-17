from django.http import HttpResponse

from django.conf import settings


REVERSE_FLAG = settings.REVERSE_FLAG
c = 0


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if self.predicate():
            r = response.content.decode()
            if REVERSE_FLAG:
                if response.status_code == 200 or response.status_code == 418:
                    s = self.russian_reverse(r)
                    response = HttpResponse(s, status=200)
        return response

    def predicate(self):
        global c
        c += 1
        if c == 10:
            c = 0
            return True
        return False

    def russian_reverse(self, f):
        begin = f[:6]
        end = f[-7:]
        f = f[6:-7]
        f = f.split(" ")
        new_f = ""
        ru_Alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        eng_Alp = "abcdefghijklmnopqrstuvwxyz"
        for word in f:
            cut_str = ""
            for sign in word:
                if sign.lower() in eng_Alp or sign.isdigit():
                    cut_str = word
                    break
                elif sign.lower() in ru_Alp:
                    cut_str = sign + cut_str
                else:
                    cut_str += sign
            new_f += cut_str + ' '
        return begin + new_f[:-1] + end

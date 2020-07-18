from django.http import HttpResponse
#utilities
from datetime import datetime


def helloWorld(request):
    now = datetime.now().strftime('%b %dth, %Y')
    return HttpResponse('Hello world {now}'.format(now=str(now)))


def say_hi(request, name, age):
    if age < 18:
        message = "¡Hey, {}. No tienes la edad aún".format(name)
    else:
        message = "¡Hey, {}. Bienvenido".format(name)

    return HttpResponse(message)

from django.http import HttpRequest, HttpResponse


def index(request):
    return HttpRequest('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')

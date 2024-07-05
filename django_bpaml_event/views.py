from django.http import HttpResponse


def index_page(request):
    return HttpResponse("<h1>BPAML Event</h1>")

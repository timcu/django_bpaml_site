from django.shortcuts import render


def index_page(request):
    return render(request, 'django_bpaml_event/index.html', {})


def event_page(request, code):
    return render(request, 'django_bpaml_event/event.html', {'code': code})

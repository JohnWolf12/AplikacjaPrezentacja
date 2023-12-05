from django.shortcuts import render

from AplikacjaPrzedmioty.models import Przedmiot


def index(request):
    przedmioty = Przedmiot.objects.all()
    context = {
        "przedmioty": przedmioty
    }
    return render(request, 'AplikacjaPrzedmioty/index.html', context)

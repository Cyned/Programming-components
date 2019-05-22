from django.shortcuts import render

from lab6.patterns import get_output


def index(request):
    return render(request, "index.html", {"output": get_output})

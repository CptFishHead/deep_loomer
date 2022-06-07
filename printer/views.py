from django.shortcuts import render

from printer.models import Printer


def index(request):
    context = {}
    printers = Printer.objects.all()
    context.update({"printers": printers})
    return render(request, "index.html", context)


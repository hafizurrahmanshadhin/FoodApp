from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! This is the food app index page.")


def item(request):
    return HttpResponse("This is the item page of the food app.")

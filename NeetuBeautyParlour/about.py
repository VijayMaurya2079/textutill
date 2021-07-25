from django.http import HttpResponse


def about(response):
    return HttpResponse("About Page")

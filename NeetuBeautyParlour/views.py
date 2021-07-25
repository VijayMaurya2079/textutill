# This view is created by - Vijay
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Vijay Maurya', 'designation': 'Sr Software Enginer'}
    return render(request, 'index.html', params)


def analyze(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    text = request.POST.get('text', 'NA')
    analyzed_text = ""
    purpose = ""

    if removepunc == "on":
        purpose = 'Removed  Puntuations'
        for char in text:
            if char not in punctuations:
                analyzed_text = analyzed_text+char

    elif fullcaps == "on":
        purpose = 'Full Caps'
        analyzed_text = text.upper()

    elif newlineremover == "on":
        purpose = 'Newline Remover'
        for char in text:
            if char != "\n" and char != "\r":
                analyzed_text = analyzed_text+char

    elif spaceremover == "on":
        purpose = 'Extra Space Remover'
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == ""):
                analyzed_text = analyzed_text+char

    else:
        purpose = 'Action not Selected'
        analyzed_text = text

    params = {'purpose': purpose, 'analyzed_text': analyzed_text}

    return render(request, "analyze.html", params)

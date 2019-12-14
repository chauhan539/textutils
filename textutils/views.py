# i made this
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    #  return HttpResponse("hello")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'capitlized', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

            params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}

        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char

            params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}

        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(charcounter == "on"):
        ccount = len(djtext)

        params = {'purpose': 'charcounter', 'analyzed_text': ccount}

        return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)

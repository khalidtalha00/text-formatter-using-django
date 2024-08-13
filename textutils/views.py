from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')

    if removepunc=='on':
        analyzed = ""
        punctuations= '''.…/‘“”<>{}[]()—–;:,!?.*'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to Uppercase','analyzed_text':analyzed}

        return render(request,'analyze.html',params)
    elif newlineremove=="on":
     analyzed=""
     for char in djtext:
      if char !="\n" and char!="\r":
       analyzed=analyzed+char
     params={'purpose':'Remove newline','analyzed_text':analyzed}

     return render(request,"analyze.html",params)
    elif extraspaceremove=='on':
        analyzed = ""
        length = len(djtext)
        for index in range(length):
            if not (djtext[index] == " " and index + 1 < length and djtext[index + 1] == " "):
                analyzed += djtext[index]

        params={'purpose':'Remove Extra space','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("ERROR")


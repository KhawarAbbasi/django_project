from django.http import HttpResponse
from django.shortcuts import render
def Index(request):
    return render(request,'index.html')
def analyze(request):
    text=request.GET.get('text','default')
    removepun=request.GET.get('checktext','off')
    newtext=""
    punctuations='''!()-[]{};:'"\,<>.?@#$%^&*/'''
    for char in text:
        if char not in punctuations:
            newtext=newtext+char

    params={'purpose':'Removed Punstutauton','analyzed_text':newtext}
    return render(request,'analyze.html',params)
from django.shortcuts import render
from django.http import HttpResponse
import googletrans
from googletrans import Translator
# Create your views here.
def index(request):
    return render(request,'webpage.html')
def translate(request):
    s1=request.GET['te']
    s2=request.GET['t2']
    d=googletrans.LANGUAGES
    lst1=list(d.keys())
    lst2=list(d.values())
    i=lst2.index(s2)
    t=Translator()
    s3=t.translate(str(s1),dest=str(lst1[i])).text
    return render(request,'result.html',{'inputtext':s1,'language':s2,'transl':s3})

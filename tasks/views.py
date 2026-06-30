from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
   return HttpResponse('<h1>The homepage is the default entry point of a digital property. It acts as a table of contents, a brand billboard, and a routing mechanism. Its primary goal is to answer three questions for the user within seconds:</h1>')

def about (request):
    return HttpResponse('<h2>he About page is the digital embodiment of a company’s or project’s identity:<\h2')

def contact (request):
        return HttpResponse('<h3>The Contact page is the utility hub for user communication:<\h3')
    
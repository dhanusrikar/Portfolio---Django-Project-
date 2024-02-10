from django.shortcuts import render, HttpResponse
# Create your views here.
def home(reqeust):
    return HttpResponse("This is the data")

def paths(request):
    return HttpResponse("This is a path view created by srikar.")

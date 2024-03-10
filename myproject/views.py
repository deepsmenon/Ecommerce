
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcomeview(request,name):
  return HttpResponse("This is my webpage : "  + name)

def greeting(request):
  return render(request,"greet.html")
  # return HttpResponse("Greeting 12")

def welcomescreen(request):
  return render(request,"welcome.html")

def Showdetails(request):
  greet = {
    "welcome" : "hello user",
    "fname" : "Deepa",
    "gender" : "F",
    "profile" : {
      "job": "software",
      "company": "magnus"
    },
    "num" :[1,2,3,4,5,6,7]

  }
  return render(request,"Showdetails.html", greet)
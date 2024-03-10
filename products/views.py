from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listproducts(request):
  context ={
    "name":"T-shirts",
    "size": "Small",
    "prize": 30,
    "color": "Red"
  }
  return render(request,"product.html",context)


def editproducts(request):
  return HttpResponse("Edit your products here")
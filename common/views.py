from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signin(request):
    return HttpResponse("sign in")

def signup(request):
    return render(request, "common/signup.html")

def logout(request):
    return HttpResponse("logout")
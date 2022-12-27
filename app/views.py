from django.shortcuts import render
from django.http import render
# Create your views here.
def first(request):
    return render(request,'first.html')
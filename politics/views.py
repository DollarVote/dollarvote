from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def getCompany(request):
    data = json.loads(request.body)
    return
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse

# Create your views here.


def get_company(request):
    """Returns a company's positions on listed issues to the Chrome Extension"""
    data = str(request.body)
    print("Received company: " + data)
    print(request.body)
    response_data = {
            "donations": {"support": 2647281, "oppose": 10946721},
            "title": "Serverzzzzz",
            "amount": "10946721",
            "causes": {"Has donated to pro-life causes.": {"amount"},
                        "Has supported pro-second amendment legislation.":,
                        "Supports the construction of the Mexican border wall.":,
                        "Supports Medicare for All.":,
                        "isGood": False
    }}
    response = JsonResponse(response_data)
    return response

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views import View
from chromiumextension.src.impact import calculate_impact

# Create your views here.


def get(request):
    company = str(request.body)
    print("Received company: " + company)
    response_data = calculate_impact(company)
    response = JsonResponse(response_data)
    return response


class ChromiumExtension(View):
    pass


# def get_company(request):
#     """Returns a company's positions on listed issues to the Chrome Extension"""
#     data = str(request.body)
#     print("Received company: " + data)
#     print(request.body)
#     response_data = {"blm": 0.0, "climate": 0, "healthcare": 0.0}
#     response = JsonResponse(response_data)
#     return response

from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views import View
from chromiumextension.src.impact import calculate_impact

# Create your views here.


class ChromiumExtension(View):

    def get(self, request):
        company = str(request.body)
        print("Received company: " + company)
        response_data = calculate_impact(company)
        response = JsonResponse(response_data)
        return response

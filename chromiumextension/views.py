from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views import View
from chromiumextension.src.impact import calculate_impact

# Create your views here.


class ChromiumExtension(View):

    def get(self, request):
        company = request.GET['company']
        # print("Received company: " + company)
        # print(request.GET)
        # return HttpResponse()
        response_data = calculate_impact(company)
        print(response_data)
        print(response_data.company)
        print(response_data.issue)
        print(response_data.blm)
        print(response_data.climate)
        print(response_data.healthcare)
        return HttpResponse()
        # response = JsonResponse(response_data)
        # return response

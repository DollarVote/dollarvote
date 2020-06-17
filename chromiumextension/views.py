from django.http import JsonResponse
from django.views import View
from django.core import serializers
from chromiumextension.src.impact import donation_impact


class ChromiumExtension(View):

    def get(self, request):
        company = request.GET['company']
        response_data = donation_impact(company)
        print(response_data)
        print(response_data.company)
        print(response_data.issue)
        print(response_data.blm)
        print(response_data.climate)
        print(response_data.healthcare)
        serialized_response_data = serializers.serialize('json', [ response_data, ])
        response = JsonResponse(serialized_response_data, safe=False)
        return response

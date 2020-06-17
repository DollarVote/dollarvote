from django.http import JsonResponse
from django.views import View
from django.core import serializers
from chromiumextension.src.impact import ImpactFactor


class ChromiumExtension(View):

    def get(self, request):
        company = request.GET['company']
        impact_factor = ImpactFactor(company)
        issue_impact = impact_factor.company_impact()
        serialized_response_data = serializers.serialize('json', [issue_impact, ])
        response = JsonResponse(serialized_response_data, safe=False)
        return response

from django.http import HttpResponse
from django.views import View
from chromiumextension.src.impact import ImpactFactor
from chromiumextension.models import Company
import json


class ChromiumExtension(View):

    def get(self, request):
        company_name = request.GET['company']
        company = Company.objects.filter(name=company_name).first()
        impact_factor = ImpactFactor(company.id)
        issue_impact = impact_factor.company_impact()
        for issue in issue_impact.keys():
            print(issue_impact, issue_impact[issue])
        data = json.dumps(issue_impact)
        return HttpResponse(data)

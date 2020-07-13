from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from chromiumextension.src.impact import ImpactFactor
from chromiumextension.models import Company
import json


class ChromiumExtension(View):

    def get(self, request):
        company_name = request.GET['company']
        company = Company.objects.filter(name__contains=company_name).first()
        if company is None:
            message = {"message": "Company Not Found"}
            data = json.dumps(message)
            return HttpResponse(data)
        impact_factor = ImpactFactor(company)
        issue_impact = impact_factor.company_impact()
        for issue in issue_impact.keys():
            print(issue_impact, issue_impact[issue])
        issue_impact["company"] = company.name
        data = json.dumps(issue_impact)
        return HttpResponse(data)

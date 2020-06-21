from django.views import View
from django.http import HttpResponse
import json


class DollarVote(View):

    def get(self, _):
        message = {"message": "Hello World! Vote with your dollars with DollarVote."}
        data = json.dumps(message)
        return HttpResponse(data)

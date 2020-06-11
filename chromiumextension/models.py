from django.db import models


class Candidate(models.Models):
    """Class that specifies a political Candidate"""
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)


class Stance(models.Models):
    """Links political candidates to all their stances on issues"""
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    issue = models.CharField(max_length=128)
    stance = models.CharField(max_length=128)


class Company(models.Models):
    """Company and its donations to political candidates"""
    name = models.CharField(max_legnth=128)


class Donation(models.Models):
    """Weak entity denoting donations from a specific company to a political candidate"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    amount = models.BigIntegerField()

class Issue(models.Models):
    "All issues we currently store data for"
    name = models.CharField(max_length=256)

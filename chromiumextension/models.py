from django.db import models


class Candidate(models.Model):
    """Class that specifies a political Candidate"""
    opensecrets_id = models.CharField(max_length=16, null=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Stance(models.Model):
    """Links political candidates to all their stances on issues"""
    candidate = models.CharField(max_length=16, null=False)
    issue = models.CharField(max_length=16)
    stance = models.FloatField(default=0.0)


class Company(models.Model):
    """Company and its donations to political candidates"""
    opensecrets_id = models.CharField(max_length=16, null=False)
    name = models.CharField(max_length=128, default="")
    parent_company = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class Donation(models.Model):
    """Weak entity denoting donations from a specific company to a political candidate"""
    company = models.CharField(max_length=16, null=False)
    candidate = models.CharField(max_length=16, null=False)
    amount = models.BigIntegerField()


class CompanyAttributes(models.Model):
    company_opensecrets = models.CharField(max_length=16, null=False)
    attribute = models.CharField(max_length=128, null=False)


# class Issue(models.Model):
#     """All issues for which we currently store data.
#     Temporarily unimplemented because we are using hardcoded issues."""
#     name = models.CharField(max_length=256)


class Impact(models.Model):
    """Weak entity connecting a company to issues (issues not yet implemented)"""
    company = models.CharField(max_length=16, null=False)
    # issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    issue = models.CharField(max_length=16)
    channel = models.CharField(max_length=16, default="No Type")
    score = models.FloatField(default=0.0)

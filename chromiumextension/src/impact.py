from chromiumextension.models import Donation, Stance, Impact
from chromiumextension.constants import Issues

stance_map = {"Yes": 1.0, "No": -1.0}


def calculate_impact(company):
    """TODO: Add alternate ways to calculate impact."""
    "Calculates the impact that company donations have on the issue in question."
    donation_impact = calculate_donation(company)

    return donation_impact


def calculate_donation(company):
    """TODO: This function might need to be heavily modified"""
    issue_weights = {}
    donation_total = {}
    for issue in Issues.all_issues:
        issue_weights[issue] = 0
        donation_total[issue] = 0

    all_donations = Donation.objects.filter(company__name=company)
    for donation in all_donations:
        donation_total += donation.amount
        candidate = donation.candidate
        stances = Stance.objects.filter(candidate__id=candidate.id)
        for stance in stances:
            issue_weights[stance.issue] += donation.amount * stance_map[stance.stance]
            donation_total[stance.issue] += donation.amount

    for issue in Issues.all_issues:
        issue_weights[issue] = issue_weights[issue] / donation_total[issue]
    return issue_weights

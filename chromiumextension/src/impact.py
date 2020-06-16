from chromiumextension.models import Donation, Stance, Impact
from chromiumextension.constants import Issues

stance_map = {"Yes": 1.0, "No": -1.0}


def calculate_impact(company):
    """TODO:
        1.Add alternate ways to calculate impact.
        2.Only lookup issues specific to the user."""
    "Calculates the impact that company donations have on the issue in question."
    found_impact = {}
    user_issues = Issues.all_issues
    remaining_issues = set(user_issues)

    relevant_impact = Impact.objects.filter(company=company, issue__in=user_issues)
    for impact in relevant_impact:
        found_impact[impact.issue] = impact.score
        remaining_issues.discard(impact.issue)

    remaining_impact = {}
    if remaining_issues:
        remaining_impact = calculate_donation(company, remaining_issues)

    donation_impact = {}
    donation_impact.update(found_impact)
    donation_impact.update(remaining_impact)

    return donation_impact


def calculate_donation(company, issues):
    """TODO: This function might need to be heavily modified"""
    issue_weights = {}
    donation_total = {}
    for issue in issues:
        issue_weights[issue] = 0
        donation_total[issue] = 0

    all_donations = Donation.objects.filter(company__name=company)
    for donation in all_donations:
        candidate = donation.candidate
        stances = Stance.objects.filter(candidate__id=candidate.id, issue__in=issues)
        for stance in stances:
            issue_weights[stance.issue] += donation.amount * stance_map[stance.stance]
            donation_total[stance.issue] += donation.amount

    issues_impact = {}
    for issue in issues:
        score = issue_weights[issue] / donation_total[issue]
        donation_impact = Impact(company=company, issue=issue, score=score)
        donation_impact.save()
        issues_impact[issue] = score

    return issues_impact

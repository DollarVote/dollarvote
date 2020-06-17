from chromiumextension.models import Donation, Stance, Impact
from chromiumextension.constants import Issues, ImpactChannel

stance_map = {"Yes": 1.0, "No": -1.0}


class ImpactFactor:

    def __init__(self, company):
        self.company = company
        self.issues = Issues.all_issues

    def company_impact(self):
        """Creates an aggregated score of a company's impact toward different issues.
        TODO:
            1.Only lookup issues specific to the user.
            2.Add channels only specific to the user.
            3.Customize channel weights to the user."""
        user_issues = Issues.all_issues
        user_channels = ImpactChannel.all_channels
        channel_weights = {"donation": 0.7, "pledge": 0.3}

        complete_impact = dict([(issue, 0.0) for issue in user_issues])
        for channel in user_channels:
            channel_impact = self.channel_impact(channel)
            for issue in user_issues:
                complete_impact[issue] += channel_weights[channel] * channel_impact[issue]

        return complete_impact

    def channel_impact(self, channel):
        if channel == ImpactChannel.pledge:
            return self.pledge_impact()
        elif channel == ImpactChannel.donation:
            return self.donation_impact()

    def pledge_impact(self):
        pledge = {}
        remaining_issues = set(self.issues)

        relevant_impact = Impact.objects.filter(company=self.company,
                                                channel=ImpactChannel.pledge,
                                                issue__in=self.issues)
        for impact in relevant_impact:
            pledge[impact.issue] = impact.score
            remaining_issues.discard(impact.issue)

        for issue in remaining_issues:
            pledge[issue] = 0.0

        return pledge

    def donation_impact(self):
        """Calculates the impact that company donations have on the issue in question."""
        found_impact = {}
        remaining_issues = set(self.issues)

        relevant_impact = Impact.objects.filter(company=self.company,
                                                channel=ImpactChannel.donation,
                                                issue__in=self.issues)
        for impact in relevant_impact:
            found_impact[impact.issue] = impact.score
            remaining_issues.discard(impact.issue)

        remaining_impact = {}
        if remaining_issues:
            remaining_impact = self.calculate_donation(remaining_issues)

        donation = {}
        donation.update(found_impact)
        donation.update(remaining_impact)

        return donation

    def calculate_donation(self, issues):
        """TODO: This function might need to be heavily modified"""
        issue_weights = {}
        donation_total = {}
        for issue in issues:
            issue_weights[issue] = 0
            donation_total[issue] = 0

        all_donations = Donation.objects.filter(company__name=self.company)
        for donation in all_donations:
            candidate = donation.candidate
            stances = Stance.objects.filter(candidate__id=candidate.id, issue__in=issues)
            for stance in stances:
                issue_weights[stance.issue] += donation.amount * stance_map[stance.stance]
                donation_total[stance.issue] += donation.amount

        issues_impact = {}
        for issue in issues:
            score = issue_weights[issue] / donation_total[issue]
            donation = Impact(company=self.company, channel=ImpactChannel.donation,issue=issue, score=score)
            donation.save()
            issues_impact[issue] = score

        return issues_impact

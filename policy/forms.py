from django import forms
from django.contrib.auth import get_user_model
from policy.models import Policy, Revision, RevisionStatus
from pagedown.widgets import PagedownWidget


class NewPolicyForm(forms.Form):
    name = forms.CharField(
        max_length=50, required=True,
        help_text='What should the policy be called?')

    preamble = forms.CharField(
        help_text='Why should this policy be enacted? What is the spirit of '
                  'the policy?',
        widget=PagedownWidget(), required=False
    )

    position = forms.CharField(
        help_text=('If this policy is regarding ComSSA\'s official position '
                   'regarding a topic, what should that position be?'),
        widget=PagedownWidget(), required=False
    )

    action = forms.CharField(
        help_text=('What action should be taken (either on a once-off or '
                   'ongoing basis) as a result of this policy being enacted?'),
        widget=PagedownWidget(), required=False
    )

    submitters = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        help_text='Who is submitting/has submitted the policy?'
    )

    endorsers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.filter(is_superuser=True),
        help_text='Who is endorsing/has endorsed the policy?'
    )


class AmendmentForm(forms.Form):

    preamble = forms.CharField(
        help_text=('Why should this policy be enacted? What is the spirit of '
                   'the policy?'),
        widget=PagedownWidget(), required=False
    )

    position = forms.CharField(
        help_text=('If this policy is regarding ComSSA\'s official position'
                   'regarding a topic, what should that position be?'),
        widget=PagedownWidget(), required=False
    )

    action = forms.CharField(
        help_text=('What action should be taken (either on a once-off or '
                   'ongoing basis) as a result of this policy being enacted?'),
        widget=PagedownWidget(), required=False)

    amenders = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        help_text='Who is responsible for the amendment?'
    )

    endorsers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.filter(is_superuser=True),
        help_text='Who is endorsing the amendment?'
    )

    change = forms.CharField(
        help_text='What has been changed in this amendment?', max_length=50,
    )


class StatusUpdateForm(forms.Form):
    new_status = forms.ChoiceField(
        choices=RevisionStatus.POLICY_REVISION_STATUS_CHOICES
    )

    notes = forms.CharField(
        help_text='Why are you changing the status?', max_length=50,
    )

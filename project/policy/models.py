# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from django.db import models


class Policy(models.Model):

    "A policy."

    name = models.CharField(
        max_length=50,
        help_text="What should this policy be called?")

    lock = models.BooleanField(default=False, editable=False)

    @property
    def status(self):
        """Try to assign a meaningful status to the policy.

        - If any revisions are in a state of transition:
          - Submitted.
          - Discussion Delayed.
          - In Agenda.
          these statuses represent the policy as a whole.

        - If any revision is Enacted, the status of that revision represents
          the policy as a whole.

        - Otherwise, the status of the latest revision represents the policy
          as a whole.
        """

        # actual implementation does not match docstring!?
        r = Revision.objects.filter(policy=self).order_by('-timestamp')[0]
        return r.status

    @property
    def effective_revision(self):
        """Find the effective revision of the policy."""
        for rev in self.revision_set.order_by('-timestamp'):
            if rev.status.status == "EN":
                return rev
        return self.revision_set.order_by('-timestamp')[0]

    def __str__(self):
        return self.name


class Revision(models.Model):

    """A policy revision."""

    preamble = models.TextField(blank=True)

    position = models.TextField(blank=True)

    action = models.TextField(blank=True)

    submitters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='submitters')

    endorsers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='endorsers')

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    change = models.CharField(max_length=50)

    policy = models.ForeignKey(Policy)

    @property
    def status(self):
        """Get the revision's current status."""
        return RevisionStatus.objects.filter(
            revision=self).order_by('-timestamp')[0]

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "%s: %s" % (self.policy, self.change)


class RevisionStatus(models.Model):

    """A status change on a policy revision."""

    SUBMITTED = 'SB'
    IN_AGENDA = 'AG'
    DELAYED = 'DL'
    ENACTED = 'EN'
    FAILED = 'FA'
    NULLIFIED = 'NU'
    INVALID = "IV"

    POLICY_REVISION_STATUS_CHOICES = (
        (SUBMITTED, 'Submitted'),
        (IN_AGENDA, 'In Agenda'),
        (DELAYED, 'Discussion Delayed'),
        (ENACTED, 'Enacted'),
        (FAILED, 'Failed'),
        (NULLIFIED, 'Nullified'),
        (INVALID, "Invalid"),
    )

    changer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        help_text="Who caused the status change?"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    status = models.CharField(help_text="What's the new status?",
                              choices=POLICY_REVISION_STATUS_CHOICES,
                              max_length=2)

    notes = models.CharField(max_length=50)

    revision = models.ForeignKey(Revision)

    def __str__(self):
        return self.get_status_display()

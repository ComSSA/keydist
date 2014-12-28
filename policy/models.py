from django.db import models
from django.contrib.auth import get_user_model

class Policy(models.Model):
	name = models.CharField(
		max_length = 50,
		help_text = "What should this policy be called?"
	)

	lock = models.BooleanField(
		default = False,
		editable = False
	)

	@property
	def status(self):
		r = Revision.objects.filter(policy = self).order_by('-timestamp')[0]
		return r.status
	

class Revision(models.Model):
	preamble = models.TextField(
		blank = True,
	)

	position = models.TextField(
		blank = True,
	)

	action = models.TextField(
		blank = True,
	)

	submitters = models.ManyToManyField(
		get_user_model(),
		related_name = 'submitters'
	)

	endorsers = models.ManyToManyField(
		get_user_model(),
		related_name = 'endorsers'
	)

	timestamp = models.DateTimeField(
		auto_now_add = True,
		editable = False
	)

	change = models.CharField(
		max_length = 50,
	)

	policy = models.ForeignKey(Policy)

	@property
	def status(self):
	    return RevisionStatus.objects.filter(revision = self).order_by('-timestamp')[0]

	class Meta:
		ordering = ['-timestamp']


class RevisionStatus(models.Model):
	SUBMITTED = 'SB'
	IN_AGENDA = 'AG'
	DELAYED = 'DL'
	ENACTED = 'EN'
	FAILED = 'FA'
	NULLIFIED = 'NU'

	POLICY_REVISION_STATUS_CHOICES = (
		(SUBMITTED, 'Submitted'),
		(IN_AGENDA, 'In Agenda'),
		(DELAYED, 'Delayed'),
		(ENACTED, 'Enacted'),
		(FAILED, 'Failed'),
		(NULLIFIED, 'Nullified'),
	)

	changer = models.ForeignKey(
		get_user_model(),
		editable = False,
		help_text = "Who caused the status change?"
	)

	timestamp = models.DateTimeField(
		auto_now_add = True,
		editable = False
	)

	status = models.CharField(
		help_text = "What's the new status?",
		choices = POLICY_REVISION_STATUS_CHOICES,
		max_length = 2
	)
	
	notes = models.CharField(
		max_length = 50,
	)

	revision = models.ForeignKey(
		Revision
	)

	def __str__(self):
		return self.get_status_display()

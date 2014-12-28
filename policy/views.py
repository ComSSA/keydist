from django.shortcuts import render, get_object_or_404
import forms
import models
from keydist.views import *

# Create your views here.
def write(request):
	if request.method == 'POST':
		form = forms.NewPolicyForm(request.POST)

		if form.is_valid():
			# Create a new Policy.
			p = models.Policy()
			p.name = form.cleaned_data['name']
			p.lock = True
			p.save()

			# Create the policy's first revision.
			r = models.Revision()
			r.policy = p
			r.preamble = form.cleaned_data['preamble']
			r.position = form.cleaned_data['position']
			r.action = form.cleaned_data['action']
			r.change = "Initial revision."
			r.save()

			r.submitters = form.cleaned_data['submitters']
			r.endorsers = form.cleaned_data['endorsers']

			r.save()

			# Set the status of this first revision.
			rs = models.RevisionStatus()
			rs.revision = r
			rs.status = models.RevisionStatus.SUBMITTED
			rs.changer = request.user
			rs.notes = "Initial status for first revision of policy."
			rs.save()

			p.lock = False
			p.save()
	else:
		form = forms.NewPolicyForm()

	return render(request, 'policy/write.html', {
		'form': form
	})

def amend(request, policy_id):
	try:
		target_policy = models.Policy.objects.get(pk=1)
		latest_revision = models.Revision.objects.filter(policy = policy_id).order_by('timestamp')[0]
	except models.Policy.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = forms.AmendmentForm(request.POST)
		if form.is_valid():
			# Lock the policy.
			target_policy.lock = True
			target_policy.save()

			# Create the new revision.
			r = models.Revision()
			r.policy = target_policy
			r.preamble = form.cleaned_data['preamble']
			r.position = form.cleaned_data['position']
			r.action = form.cleaned_data['action']
			r.change = form.cleaned_data['change']
			r.save()
			# ORM limitatiosn require the save
			r.submitters = form.cleaned_data['amenders']
			r.endorsers = form.cleaned_data['endorsers']
			r.save()

			# Set the initial status of this revision.
			rs = models.RevisionStatus()
			rs.revision = r
			rs.status = models.RevisionStatus.SUBMITTED
			rs.changer = request.user
			rs.notes = "Initial status for new amendment."
			rs.save()

			target_policy.lock = False
			target_policy.save()
	else:
		form = forms.AmendmentForm(initial = {
			'preamble': latest_revision.preamble,
			'position': latest_revision.position,
			'action': latest_revision.action
		})

	return render(request, 'policy/amend.html', {
		'policy': target_policy,
		'revision': latest_revision,
		'form': form
	})


class PolicyList(TheofficeListView):
	model = models.Policy
	template_name = 'policy/list.html'

	def get_context_data(self, **kwargs):
		context = super(PolicyList, self).get_context_data(**kwargs)
		context['status_update_note_form'] = forms.StatusUpdateNoteForm()
		return context


def update_status(request, revision_id):
	revision = get_object_or_404(models.Revision, pk = revision_id)
	return render(request, 'policy/update_status.html', {
		'revision': revision,
		'form': forms.StatusUpdateForm()
	})
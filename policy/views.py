from django.shortcuts import render, get_object_or_404, redirect
import forms
import models
from theoffice.views import *
from django.contrib import messages


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
			
			messages.success(request, "The policy has been submitted for secretarial approval.")
			return redirect("policy:list")
	else:
		form = forms.NewPolicyForm()

	return render(request, 'policy/write.html', {
		'form': form
	})

def amend(request, policy_id):
	try:
		target_policy = models.Policy.objects.get(pk = policy_id)
		latest_revision = models.Revision.objects.filter(policy = policy_id).order_by('timestamp')[0]
	except models.Policy.DoesNotExist:
		raise Http404

	if request.method == 'POST':
		form = forms.AmendmentForm(request.POST)
		if form.is_valid():
			if target_policy.lock is not True:
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
				r.save() # ORM limitatiosn require the save
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
				return redirect("policy:list")
			else:
				messages.error(request, "The policy has been edit locked. Please try again in a moment.")
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

def update_status(request, revision_id):
	revision = get_object_or_404(models.Revision, pk = revision_id)
	
	if request.method == 'POST':
		form = forms.StatusUpdateForm(request.POST)
		
		if form.is_valid():
			if revision.policy.lock is True:
				messages.error(request, "The policy has been edit locked. Please try again in a moment.")
			else:
				# Lock the policy.
				revision.policy.lock = True
				revision.policy.save()
				
				# Add the new status.
				s = models.RevisionStatus()
				s.changer = request.user
				s.status = form.cleaned_data['new_status']
				s.notes = form.cleaned_data['notes']
				s.revision = revision
				s.save()
				
				revision.policy.lock = False
				revision.policy.save()
			
				messages.success(request, "The revision has been updated successfully.")
				return redirect('policy:list')
	else:
		form = forms.StatusUpdateForm()
	return render(request, 'policy/update_status.html', {
		'revision': revision,
		'form': form
	})

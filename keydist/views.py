from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class KeydistCreateView(CreateView):
	template_name = 'generic_form.html'

class KeydistUpdateView(UpdateView):
	template_name = 'generic_form.html'

class KeydistDetailView(DetailView):
	template_name = 'generic_detail.html'

class KeydistListView(ListView):
	template_name = 'generic_list.html'

class KeydistDeleteView(DeleteView):
	template_name = 'generic_delete.html'
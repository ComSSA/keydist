from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class TheofficeCreateView(CreateView):
    template_name = 'generic_form.html'


class TheofficeUpdateView(UpdateView):
    template_name = 'generic_form.html'


class TheofficeDetailView(DetailView):
    template_name = 'generic_detail.html'


class TheofficeListView(ListView):
    template_name = 'generic_list.html'


class TheofficeDeleteView(DeleteView):
    template_name = 'generic_delete.html'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import UpdateView

from .forms import *
from .models import *

# Create your views here.
class ExpertSearch(TemplateView):

    def get_template_names(self):
        """
        if this is a search request, return the search results template, else
        return the homepage template.
        """
        if self.request.GET.get('q'):
            return ['expert_search/search_results.html']
        else:
            return ['expert_search/search_home.html']


class ContributeHome(LoginRequiredMixin, TemplateView):
    """
    Simple FormView for contributing experts. Requires authentication.
    """
    template_name = 'contributors/home.html'

    def get_context_data(self, **kwargs):
        expert_list = Expert.objects.all()
        return { 'expert_list': expert_list }

def contribute_logout(request):
    return logout_then_login(request,
        login_url=reverse_lazy('contribute_login'))


class ContributeExpertDetail(LoginRequiredMixin, TemplateView):
    """
    View for viewing the details of an Expert.
    """
    template_name = 'contributors/expert_detail.html'

    def get_context_data(self, **kwargs):
        try:
            expert = Expert.objects.get(pk=self.kwargs['pk'])
            return { 'expert': expert }
        except Expert.DoesNotExist:
            raise Http404


class ContributeAddExpert(LoginRequiredMixin, FormView):
    """
    View for adding an individual Expert.
    """
    template_name = 'contributors/expert_form.html'
    form_class = ExpertForm
    success_url = reverse_lazy('contribute_home')
    login_url = reverse_lazy('contribute_login')

    def form_valid(self, form):
        form.save()
        return super(ContributeAddExpert, self).form_valid(form)


class ContributeExpertUpdate(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing Expert.
    """
    model = Expert
    fields = ('title', 'first_name', 'last_name', 'affiliation', 'subjects',
        'fields', 'website', 'description')
    template_name = 'contributors/expert_form.html'


class ContributeExpertDelete(LoginRequiredMixin, TemplateView):
    pass
    # TODO: Finish implementation of delete view


class ContributeAddField(LoginRequiredMixin, FormView):
    """
    View for adding an individual Field.
    """
    template_name = 'contributors/add_field.html'
    form_class = FieldForm
    success_url = reverse_lazy('contribute_home')
    login_url = reverse_lazy('contribute_login')

    def form_valid(self, form):
        form.save()
        return super(ContributeAddField, self).form_valid(form)

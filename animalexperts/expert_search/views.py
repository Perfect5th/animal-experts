from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .forms import ExpertForm

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


class ContributeAddExpert(LoginRequiredMixin, FormView):
    """
    Dashboard view for contributors.
    """
    template_name = 'contributors/add_expert.html'
    form_class = ExpertForm
    success_url = reverse_lazy('contribute_home')
    login_url = reverse_lazy('contribute_login')


class ContributeHome(LoginRequiredMixin, TemplateView):
    """
    Simple FormView for contributing experts. Requires authentication.
    """
    template_name = 'contributors/home.html'

def contribute_logout(request):
    return logout_then_login(request,
        login_url=reverse_lazy('contribute_login'))

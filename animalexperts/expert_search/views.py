from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ExpertSearch(TemplateView):
    
    def get_template_names(self):
        """
        if this is a search request, return the search results template, else 
        return the homepage template
        """
        if self.request.GET.get('q'):
            return ['expert_search/search_results.html']
        else:
            return ['expert_search/search_home.html']

from django.forms import ModelForm

from .models import Expert


class ExpertForm(ModelForm):
    class Meta:
        model = Expert
        fields = ['title', 'first_name', 'last_name',
            'affiliation', 'subjects', 'fields', 'email',
            'website', 'description']

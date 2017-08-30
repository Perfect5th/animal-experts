from django.forms import ModelForm
from django.utils.text import slugify

from .models import *


class ExpertForm(ModelForm):
    class Meta:
        model = Expert
        fields = ['title', 'first_name', 'last_name', 'affiliation', 'subjects',
            'fields', 'website', 'description']


class FieldForm(ModelForm):

    def save(self, *args, **kwargs):
        self.cleaned_data['code'] = slugify(self.cleaned_data['name'])
        return super(FieldForm, self).save(*args, **kwargs)

    class Meta:
        model = FieldCategory
        fields = ['name',]

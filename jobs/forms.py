from django import forms
from jobs.models import Job, REGIONS as baseRegions, JOB_TYPES

REGIONS = tuple([('all', 'All')] + list(baseRegions))

ORDER = (
    ("newest to oldest", "Newest to Oldest"), ("region: a to z", "Region: A to Z"), ("region: z to a", "Region: Z to A")
)


class FilterForm(forms.Form):
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=JOB_TYPES)
    order = forms.ChoiceField(widget=forms.Select, choices=ORDER)
    region = forms.ChoiceField(widget=forms.Select, choices=REGIONS)


class CommentForm(forms.Form):
    message = forms.CharField(max_length=320, label='Comment', widget=forms.Textarea(attrs={"rows": 4}),
                              help_text='ℹ️ Markdown supported')


class JobForm(forms.ModelForm):
    description = forms.CharField(max_length=1000, widget=forms.Textarea)

    class Meta:
        model = Job
        exclude = ['posted_by', 'uid']

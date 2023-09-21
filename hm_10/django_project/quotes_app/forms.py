from django import forms
from .models import Authors, Quotes


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['fullname', 'born_location', 'born_date', 'description']


class QuoteEditForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ['tags', 'author', 'quote']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Authors.objects.all()

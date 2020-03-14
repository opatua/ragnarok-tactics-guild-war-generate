from django import forms

from duapola_backend.models import Country


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
        )

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

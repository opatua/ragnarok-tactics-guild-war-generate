from django import forms

from duapola_backend.models import Currency


class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
            'minor_unit',
        )

    def __init__(self, *args, **kwargs):
        super(CurrencyForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

from django import forms

from duapola_backend.models import Color


class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = (
            'name',
            'code',
        )
        widgets = {
            'code': forms.widgets.TextInput(attrs={'type': 'color'}),
        }

    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

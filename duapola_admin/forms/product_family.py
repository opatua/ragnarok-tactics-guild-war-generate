from django import forms

from duapola_backend.models import ProductFamily


class ProductFamilyForm(forms.ModelForm):

    class Meta:
        model = ProductFamily
        fields = (
            'name',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(ProductFamilyForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

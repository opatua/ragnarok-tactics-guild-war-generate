from django import forms

from duapola_backend.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'product_family',
            'name',
            'sku',
            'quantity',
            'currency',
            'price',
        )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

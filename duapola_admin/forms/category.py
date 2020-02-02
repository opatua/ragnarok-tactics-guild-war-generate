from django import forms

from duapola_backend.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
            'name',
            'description',
            'parent_category',
        )

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

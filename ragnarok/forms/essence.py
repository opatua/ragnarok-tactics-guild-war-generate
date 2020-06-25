from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Essence, EssenceElement


class EssenceForm(forms.ModelForm):

    class Meta:
        model = Essence
        fields = (
            'name',
            'type',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(EssenceForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


class EssenceElementForm(forms.ModelForm):
    class Meta:
        model = EssenceElement
        fields = (
            'essence',
            'element',
        )

    def __init__(self, *args, **kwargs):
        super(EssenceElementForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


EssenceElementFormset = inlineformset_factory(
    Essence,
    EssenceElement,
    form=EssenceElementForm,
    extra=1,
    can_delete=True,
)

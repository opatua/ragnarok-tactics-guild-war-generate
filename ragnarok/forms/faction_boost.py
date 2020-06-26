from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import FactionBoost, FactionBoostAttribute


class FactionBoostForm(forms.ModelForm):

    class Meta:
        model = FactionBoost
        fields = (
            'name',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(FactionBoostForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


class FactionBoostAttributeForm(forms.ModelForm):
    class Meta:
        model = FactionBoostAttribute
        fields = (
            'faction_boost',
            'faction',
            'quantity',
        )

    def __init__(self, *args, **kwargs):
        super(FactionBoostAttributeForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


FactionBoostAttributeFormset = inlineformset_factory(
    FactionBoost,
    FactionBoostAttribute,
    form=FactionBoostAttributeForm,
    extra=1,
    can_delete=True,
)

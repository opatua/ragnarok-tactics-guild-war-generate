from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Resonance, ResonaceRecipe


class ResonanceForm(forms.ModelForm):

    class Meta:
        model = Resonance
        fields = (
            'name',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(ResonanceForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


class ResonaceRecipeForm(forms.ModelForm):
    class Meta:
        model = ResonaceRecipe
        fields = (
            'resonance',
            'element',
            'quantity',
        )

    def __init__(self, *args, **kwargs):
        super(ResonaceRecipeForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


ResonaceRecipeFormset = inlineformset_factory(
    Resonance,
    ResonaceRecipe,
    form=ResonaceRecipeForm,
    extra=1,
    can_delete=True,
)

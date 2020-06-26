from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Resonance, ResonanceRecipe


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


class ResonanceRecipeForm(forms.ModelForm):
    class Meta:
        model = ResonanceRecipe
        fields = (
            'resonance',
            'element',
            'quantity',
        )

    def __init__(self, *args, **kwargs):
        super(ResonanceRecipeForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


ResonanceRecipeFormset = inlineformset_factory(
    Resonance,
    ResonanceRecipe,
    form=ResonanceRecipeForm,
    extra=1,
    can_delete=True,
)

from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Simulator, SimulatorAttribute


class SimulatorForm(forms.ModelForm):

    class Meta:
        model = Simulator
        fields = (
            'id',
        )

    def __init__(self, *args, **kwargs):
        super(SimulatorForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                    'readonly': True,
                }
            )


class SimulatorAttributeForm(forms.ModelForm):
    class Meta:
        model = SimulatorAttribute
        fields = (
            'simulator',
            'monster',
            'essence',
        )

    def __init__(self, *args, **kwargs):
        super(SimulatorAttributeForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


SimulatorAttributeFormset = inlineformset_factory(
    Simulator,
    SimulatorAttribute,
    form=SimulatorAttributeForm,
    extra=1,
    can_delete=True,
)

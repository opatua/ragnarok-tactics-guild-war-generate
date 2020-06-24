from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Character, Team


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = (
            'user',
            'name',
        )

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = (
            'character',
            'point',
        )

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


TeamFormset = inlineformset_factory(
    Character,
    Team,
    form=TeamForm,
    extra=1,
    can_delete=True,
)

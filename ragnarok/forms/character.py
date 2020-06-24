from django import forms

from ragnarok.models import Character


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = (
            'user',
            'name',
            'point',
        )

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

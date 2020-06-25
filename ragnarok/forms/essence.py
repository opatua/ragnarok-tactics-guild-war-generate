from django import forms

from ragnarok.models import Essence


class EssenceForm(forms.ModelForm):

    class Meta:
        model = Essence
        fields = (
            'name',
            'type',
            'element',
        )

    def __init__(self, *args, **kwargs):
        super(EssenceForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })

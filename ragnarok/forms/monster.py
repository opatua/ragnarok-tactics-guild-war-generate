from django import forms
from django.forms.models import inlineformset_factory

from ragnarok.models import Monster, MonsterElement


class MonsterForm(forms.ModelForm):

    class Meta:
        model = Monster
        fields = (
            'name',
            'faction',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(MonsterForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


class MonsterElementForm(forms.ModelForm):
    class Meta:
        model = MonsterElement
        fields = (
            'monster',
            'element',
        )

    def __init__(self, *args, **kwargs):
        super(MonsterElementForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', })


MonsterElementFormset = inlineformset_factory(
    Monster,
    MonsterElement,
    form=MonsterElementForm,
    extra=1,
    can_delete=True,
)

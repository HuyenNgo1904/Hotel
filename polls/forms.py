from django import forms
from .models import *


class RoomKindForm(forms.ModelForm):
    class Meta:
        model = RoomKind
        fields = ('idKind', 'nameKind', 'price', 'descript')


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ('idFloor', 'nameFloor')


class RoomForm(forms.ModelForm):
    # floor = forms.ModelChoiceField(queryset=Floor.objects.all(),
    #                                 empty_label="............")
    # kind = forms.ModelChoiceField(queryset=RoomKind.objects.all(),
    #                                 empty_label="............")
    class Meta:
        model = Room
        fields = ('idRoom', 'floor', 'kind', 'nameRoom', 'status')
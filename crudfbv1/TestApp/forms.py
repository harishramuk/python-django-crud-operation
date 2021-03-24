from django import forms
from TestApp.models import Parcel

class Parcelform(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'

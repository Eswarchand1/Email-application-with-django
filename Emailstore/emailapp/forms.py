from django import forms
from .models import *


class SetProfileForm(forms.ModelForm):
    class Meta:
        model = getprofileData
        fields = ('choosefile','pname','pmail','pdate','pcountry','paddress','pnumber','pprofession','ppass','prpass','pid')
    def save(self, commit=True):
        send = super(SetProfileForm, self).save(commit=False)
        if commit:
            send.save()
        return send

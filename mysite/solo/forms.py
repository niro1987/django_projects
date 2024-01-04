from django import forms


class BasicForm(forms.Form):
    field1 = forms.CharField(label="Field 1")
    field2 = forms.CharField(label="Field 2")

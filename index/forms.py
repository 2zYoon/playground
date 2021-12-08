from django import forms

class TestForm(forms.Form):
    title = forms.CharField()
    desc = forms.CharField()
from django import forms

class InputForm(forms.Form):
    input_1 = forms.CharField(label='in_1', max_length=100)
    input_2 = forms.CharField(label='in_2', max_length=100)
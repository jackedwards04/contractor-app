from django import forms

class CodeForm(forms.Form):
  your_code = forms.CharField(label='', max_length=8, min_length=8)

from django import forms
from django.core import validators

# Forms and Form validation

# def check_for_z(value):
#   if value[0].lower() != 'z':
#     raise forms.ValidationError('NAME NEEDS TO START WITH THE LETTER Z')

# class FormName(forms.Form):
#   name = forms.CharField(validators=[check_for_z])
#   email = forms.EmailField()
#   text = forms.CharField(widget=forms.Textarea)
#   botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

  # validators=[validators.MaxLengthValidator(0)] replaces the following:

  # def clean_botcatcher(self):
  #   botcatcher = self.clean_data['botcatcher']
  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError('GOTCHA BOT')
  #   return botcatcher


# Cleaning entire form at once

class FormName(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Confirm Email')
  text = forms.CharField(widget=forms.Textarea)
  
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['verify_email']

    if email != vmail:
      raise forms.ValidationError('MAKE SURE THE EMAILS MATCH')
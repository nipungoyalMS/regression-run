# forms.py
from django import forms

class RunForm(forms.Form):
    Block = forms.CharField(label='Block', widget=forms.TextInput(attrs={'placeholder': 'Type or select from dropdown'}), required=False)
    Program = forms.CharField(label='Program', widget=forms.Select(choices=[('', '---------'), ('choice1', 'Choice 1'), ('choice2', 'Choice 2')]), required=False)
    Build_path = forms.CharField(label='Build path', widget=forms.Select(choices=[('', '---------'), ('choice1', 'Choice 1'), ('choice2', 'Choice 2')]), required=False)
    Program_setup = forms.CharField(label='Program setup', widget=forms.Select(choices=[('', '---------'), ('choice1', 'Choice 1'), ('choice2', 'Choice 2')]), required=False)

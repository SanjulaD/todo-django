from django import forms

class TodoListForms(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Enter todo e.g Wash the car',
                                      'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn'}))

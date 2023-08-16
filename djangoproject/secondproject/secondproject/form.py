from django import forms

# create form using django

class usersForm(forms.Form):
    num1 = forms.CharField(label="value 1",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    # num2 = forms.CharField(label="value 2",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
  
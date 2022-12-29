from django import forms

SHIFTS=(("1","Morning"),("2","Afternoon"),("3","Evening"),)

class InputForm(forms.Form):
    firstName=forms.CharField(max_length=200)
    lastName=forms.CharField(max_length=200)
    shitf=forms.ChoiceField(choices=SHIFTS)
    time_log=forms.TimeField()
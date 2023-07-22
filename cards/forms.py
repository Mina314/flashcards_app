from django import forms

class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    #  the Boolean value set to True if you know the answer and False if you don’t
    solved = forms.BooleanField(required=False)


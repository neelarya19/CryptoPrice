from django import forms

Crypto_choice=[
    ('1','Bitcoin'),
]

class CryptoForm(forms.Form):
    crypto=forms.ChoiceField(choices=Crypto_choice)
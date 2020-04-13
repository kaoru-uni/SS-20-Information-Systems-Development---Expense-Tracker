from django import forms

card_type = [
    ('visa', 'Visa'),
    ('mastercard', 'Mastercard'),
    ('cash', 'Cash'),
]

class PaymentForm(forms.Form):
    type=forms.CharField(label='What is your card type?',
                              widget=forms.Select(choices=card_type))
    date=forms.DateField()
    amount=forms.CharField()
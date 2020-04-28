from django import forms

card_type = [
    ('visa', 'Visa'),
    ('mastercard', 'Mastercard'),
    ('cash', 'Cash'),
]


class DateInput(forms.DateInput):
    input_type = 'date'


class PaymentForm(forms.Form):
    type = forms.CharField(label='What is your card type?',
                           widget=forms.Select(choices=card_type))
    date = forms.DateField(widget=DateInput)
    amount = forms.DecimalField()

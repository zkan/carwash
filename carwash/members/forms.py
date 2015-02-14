import datetime

from django import forms

from .models import Member
from .utils import get_days, get_months, get_years


class MemberForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=300,
        required=True
    )

    last_name = forms.CharField(
        label='Last Name',
        max_length=300,
        required=True
    )

    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(),
        required=True
    )

    birth_day = forms.ChoiceField(
        label='Birth Day',
        choices=get_days(),
        required=True
    )

    birth_month = forms.ChoiceField(
        label='Birth Month',
        choices=get_months(),
        required=True
    )

    birth_year = forms.ChoiceField(
        label='Birth Year',
        choices=get_years(),
        required=True
    )

    phone = forms.CharField(
        label='Phone',
        max_length=100,
        required=True
    )

    def save(self):
        data = self.cleaned_data

        day = int(data['birth_day'])
        month = int(data['birth_month'])
        year = int(data['birth_year'])

        member = Member()
        member.first_name = data['first_name']
        member.last_name = data['last_name']
        member.email = data['email']
        member.birthdate = datetime.date(year, month, day)
        member.phone= data['phone']
        member.save()

from django import forms
from .models import Profile, TransferHistory

class ProfileForm(forms.ModelForm):
    dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD', required=False)
    phone_no = forms.CharField(label='Mobile No', max_length=12, required=False)
    res_add = forms.CharField(label='Address', max_length=120, required=False)
    res_city = forms.CharField(label='City', max_length=30, required=False)
    res_state = forms.CharField(label='State', max_length=30, required=False)

    class Meta:
        model = Profile
        fields = ['dob', 'phone_no', 'res_add', 'res_city', 'res_state']

class TransferForm(forms.Form):
    to_user = forms.CharField(help_text='Email of User to Transfer', max_length=50)
    amount = forms.FloatField(help_text='Amount to Transfer', min_value=1)

class AddMoneyForm(forms.Form):
    amount = forms.FloatField(help_text="Enter the Amount", min_value=10)

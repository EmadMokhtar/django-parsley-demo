from django import forms
from parsley.decorators import parsleyfy


@parsleyfy
class UserProfileForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    name = forms.CharField(min_length=3, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_1 = forms.CharField(widget=forms.PasswordInput(), required=True,
                                 label='Confirm password')

    class Meta:
        parsley_extras = {
            'password_1': {
                'equalto': "password",
                'error-message': "Your passwords do not match.",
            },
        }

from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=70, widget=forms.PasswordInput)

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=100,
                            widget=forms.EmailInput())

    def clean_username(self):
        """username unique """
        username = self.cleaned_data['username']
        query = User.objects.filter(username=username).exists()

        if query:
            raise forms.ValidationError('Username in use')
        return username

    def clean(self):
        """verify passwords match"""
        data = super().clean()

        password = data['password']
        password_conf = data['password_confirmation']

        if password != password_conf:
            raise forms.ValidationError('passwords do no match')

        return data

    def save(self):
        """create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

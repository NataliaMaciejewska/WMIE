import logging

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import NewUser




# tworzenie uzytkownika
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")
    sex = forms.ChoiceField(choices=[('Mężczyzna', 'Mężczyzna'), ('Kobieta', 'Kobieta')])  # Choices for sex field
    voivodeship = forms.ChoiceField(choices=[('Dolnośląskie', 'Dolnośląskie'),
                                             ('Kujawsko-pomorskie', 'Kujawsko-pomorskie'),
                                             ('Lubelskie', 'Lubelskie'),
                                             ('Lubuskie', 'Lubuskie'),
                                             ('Łódzkie', 'Łódzkie'),
                                             ('Małopolskie', 'Małopolskie'),
                                             ('Mazowieckie', 'Mazowieckie'),
                                             ('Opolskie', 'Opolskie'),
                                             ('Podkarpackie', 'Podkarpackie'),
                                             ('Podlaskie', 'Podlaskie'),
                                             ('Pomorskie', 'Pomorskie'),
                                             ('Śląskie', 'Śląskie'),
                                             ('Świętokrzyskie', 'Świętokrzyskie'),
                                             ('Warmińsko-mazurskie', 'Warmińsko-mazurskie'),
                                             ('Wielkopolskie', 'Wielkopolskie'),
                                             ('Zachodniopomorskie', 'Zachodniopomorskie')])

    class Meta:
        model = NewUser
        fields = ['email', 'sex', 'voivodeship', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save(using='users')
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            NewUser.objects.using('users').get(email=email)
            raise ValidationError("New user with this Email address already exists.")
        except NewUser.DoesNotExist:
            pass
        return email


class LoginUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')



        if email and password:
            user = authenticate(username=email, password=password)

            if not user:
                raise forms.ValidationError('User Does Not Exist')

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

        return super(LoginUserForm, self).clean(*args, **kwargs)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

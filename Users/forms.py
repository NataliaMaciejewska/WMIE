from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser


# ------- tych importow nie ruszac

# tworzenie uzytkownika --- nie ruszac!!!
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


##### --- dotad dobrze

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

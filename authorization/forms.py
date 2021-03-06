from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    password1 = forms.CharField(
        label=("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=("Подтвердите пароль"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    name = forms.CharField(required=True, max_length=30, label='Имя')

    error_messages = {
        'password_mismatch': ('The two password fields didn’t match.'),
        'user_exists': ('This email exists.')
    }

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name']

    def clean_email(self):
        username = self.cleaned_data.get("email")
        try:
            User._default_manager.get(username=username)
            # if the user exists, then let's raise an error message
            raise forms.ValidationError(
                self.error_messages['user_exists'],  # my error message
                code='user_exists',  # set the error message key
            )
        except User.DoesNotExist:
            return username  # if user does not exist so we can continue the registration process

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.first_name = self.cleaned_data['name']
        user.is_active = False
        user.save()
        return user






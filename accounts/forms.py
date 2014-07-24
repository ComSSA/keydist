from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
import lockout

class LoginForm(forms.Form):
    error_css_class = ""
    curtin_id = forms.CharField(
        widget = forms.TextInput(attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Curtin ID'}),
        max_length = 140,
        required = True
        )

    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Password'})
        )
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        curtin_id = cleaned_data.get('curtin_id')
        password = cleaned_data.get('password')
        if curtin_id and password:
            try:
                self.user = authenticate(curtin_id=curtin_id, password=password)
                if self.user is not None:
                    if self.user.is_active:
                        return cleaned_data
                    else:
                        raise forms.ValidationError('User has been disabled.', code = 'disabled')
                else:
                    raise forms.ValidationError('Invalid ID/password combination.', code = 'invalid')
            except lockout.LockedOut:
                raise forms.ValidationError('You have been locked out due to too many attempts.', code = 'lockedout')

class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(
        get_user_model().objects.all(),
        widget = forms.Select(attrs = {
            'class': 'col-md-4'
            })
        )

class AdminChangePasswordForm(forms.Form):
    user = forms.ModelChoiceField(
        get_user_model().objects.all(),
        widget = forms.Select(attrs = {
            'class': 'col-md-4'
        })
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {
            'class': 'col-md-4'
        })
    )

class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
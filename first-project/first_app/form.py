from django import forms
from django.core import validators
from first_app.models import WebPage, UserProfileInfo
from django.contrib.auth.models import User


def customized_validate_function(value):
    # implement the customized validation step
    if value[0] != 'z':
        raise forms.ValidationError("The first letter is not 'z'!")


class FormName(forms.Form):
    name = forms.CharField(validators=[customized_validate_function])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    # this is a hidden input that bots will fill them, and human cannot fill them
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # handle by hand
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOT BOT")
    #     return botcatcher

    # to clean entire form
    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vmail = all_cleaned_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email does not match")


class NewWebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

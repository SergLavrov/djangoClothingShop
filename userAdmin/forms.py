from django import forms

# username = request.POST.get('username')
# email = request.POST.get('email')
# password = request.POST.get('password')
# confirm_password = request.POST.get('confirm_password')

# ВСЕ поля-классы можно посмотреть в документации на django.forms - FORM fields
# Справочно/Важно: классы CharField, EmailField и т.д. берутся из модуля (ветки) django.forms,
# а не из модуля (ветки) models !!!


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(label='Phone', max_length=20)
    postcode = forms.CharField(label='Postcode', max_length=6)
    about = forms.CharField(label='About', widget=forms.Textarea)



# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(label='username', max_length=100)
#     email = forms.EmailField(label='email', max_length=100)
#     password = forms.CharField(label='password', max_length=100)
#     confirm_password = forms.CharField(label='Repeat password', max_length=100)

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['confirm_password']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['confirm_password']
    # def save(self):
    #     pass


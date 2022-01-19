from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField() # Email input type
    password = forms.CharField(widget=forms.PasswordInput) # Password input type

    def clean(self): # Form.cleaned_data 정의, Form's vaildation
        email = self.cleaned_data.get("email") # cleaned_data = a dictionary which survived from field's clean
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=email) # username을 email로 갖고 있는 User, username/password 회원가입 때 정의?
            if user.check_password(password):
                return self.cleaned_data
            else: # Wrong password
                raise forms.ValidationError("Wrong password!") # Form becomes invalid, li로 message 나타남
        except User.DoesNotExist:
            raise forms.ValidationError("No user!") # Form becomes invalid
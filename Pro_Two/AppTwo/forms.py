from django import forms
from AppTwo.models import Users

class user_sign_up(forms.ModelForm):
    #form fields for custom validation(None)

    class Meta:
        model = Users
        fields = "__all__"

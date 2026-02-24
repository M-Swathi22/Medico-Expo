from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def clean_mobilenumber(self):
        mobile = self.cleaned_data.get('mobilenumber')

        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")

        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")

        return mobile
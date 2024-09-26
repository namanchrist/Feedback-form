from django import forms

class FeedbackForm(forms.Form):
    username = forms.CharField(max_length=100, label='User Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), label='Confirm Password')
    phone_number = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    feedback_message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your feedback'}), label='Feedback Message')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        # Passwords must match
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        # Phone number must be digits only and at least 10 characters
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if phone_number and len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")

from django import forms
from .models import PatientFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = ["p_name", "p_email", "doc_name", "rating", "comments"]

        widgets = {
            "p_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "p_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "doc_name": forms.Select(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 1, "max": 5, "placeholder": "Rate from 1 to 5"}),
            "comments": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your feedback", "rows": 4}),
        }

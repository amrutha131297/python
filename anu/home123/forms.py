from django import forms
from .models import Book

class BookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["p_name", "p_phone", "p_email", "doc_name", "booking_date"]
        widgets = {
            "p_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "p_phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter 10-digit phone number"}),
            "p_email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "doc_name": forms.Select(attrs={"class": "form-control"}),
            "booking_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

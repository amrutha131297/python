import json
from django.db import models


class Department(models.Model):
    dep_name = models.CharField(max_length=100, verbose_name="Department Name")
    dep_description = models.TextField(verbose_name="Description")

    class Meta:
        ordering = ['dep_name']  # Sort by name alphabetically

    def __str__(self):
        return self.dep_name





class Doctor(models.Model):
    name = models.CharField(max_length=255, help_text="Full name of the doctor")
    
    specialization = models.CharField(max_length=255, help_text="Doctor's specialization (e.g., Cardiology, Neurology)")
    
    department = models.ForeignKey(
        'Department', 
        on_delete=models.CASCADE, 
        related_name="doctors",
        help_text="Department to which the doctor belongs"
    )
    
    image = models.ImageField(
        upload_to='doctors/', 
        blank=True, 
        null=True, 
        help_text="Doctor's profile picture"
    )
    
    qualification = models.CharField(max_length=255, help_text="Educational qualifications (e.g., MBBS, MD)")
    
    experience = models.PositiveIntegerField(help_text="Years of experience")
    
    timings = models.CharField(
        max_length=255, 
        help_text="Available timings (e.g., 9 AM - 5 PM)"
    )
    
    availability = models.TextField(
        default="[]", 
        help_text="JSON-formatted availability slots"
    )

    def get_availability(self):
        """ Convert availability field from string to list safely. """
        try:
            return json.loads(self.availability)
        except json.JSONDecodeError:
            return []

    def set_availability(self, availability_list):
        """ Set availability field as JSON string. """
        if isinstance(availability_list, list):
            self.availability = json.dumps(availability_list)
        else:
            raise ValueError("Availability must be a list.")

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization} ({self.department.dep_name})"




    

from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.db import models

class Book(models.Model):
    p_name = models.CharField(max_length=255, verbose_name="Patient Name")
    p_phone = models.CharField(max_length=10, verbose_name="Phone Number")
    p_email = models.EmailField(verbose_name="Email")
    doc_name = models.ForeignKey("Doctor", on_delete=models.CASCADE, verbose_name="Doctor Name")
    booking_date = models.DateField(verbose_name="Booking Date")  
    booked_on = models.DateField(auto_now=True, verbose_name="Booked On")  # Auto-set to today's date

    def clean(self):
        """Validate booking date - it should be within the next 10 days"""
        today = date.today()
        max_booking_date = today + timedelta(days=10)

        if self.booking_date < today:
            raise ValidationError("Booking date cannot be in the past.")

        if self.booking_date > max_booking_date:
            raise ValidationError(f"Booking date cannot be more than 10 days from today ({max_booking_date}).")
        

    def save(self, *args, **kwargs):
        """Run validation before saving"""
        self.clean()  # Enforce validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.p_name} - {self.doc_name} ({self.booking_date})"


from datetime import date

class PatientFeedback(models.Model):
    """Model to store patient feedback for doctors and hospital services."""
    
    p_name = models.CharField(max_length=255, verbose_name="Patient Name")
    p_email = models.EmailField(verbose_name="Email")
    doc_name = models.ForeignKey("Doctor", on_delete=models.CASCADE, verbose_name="Doctor Name")
    rating = models.IntegerField(
        choices=[(1, "⭐"), (2, "⭐⭐"), (3, "⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (5, "⭐⭐⭐⭐⭐")],
        verbose_name="Rating"
    )
    comments = models.TextField(verbose_name="Feedback Comments", blank=True)
    submitted_on = models.DateField(auto_now_add=True, verbose_name="Submitted On")

    def __str__(self):
        return f"Feedback by {self.p_name} - {self.rating} Stars"

from django.shortcuts import render,redirect
from .models import Department,Doctor,Book,PatientFeedback
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    context = {
        'dept': Department.objects.all()
    }
    return render(request, 'departments.html', context)


def doctors(request): 
    context = {
        'dos': Doctor.objects.all() 
        
    }
    return render(request, 'doctors.html', context)

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm

def booking(request):
    """Handles doctor appointment booking with form validation and success/error messages."""
    
    form = BookingForm()  # Initialize an empty form
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "✅ Your appointment has been successfully confirmed! Our team will contact you shortly with further details.")

        form = BookingForm()  # Reset the form after successful submission

    return render(request, "book_appointment.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .form import FeedbackForm  # ✅ Ensure the correct import

def feedback(request):
    """Handles patient feedback submission."""
    
    form = FeedbackForm()  # ✅ Initialize form to avoid UnboundLocalError

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Thank you for your feedback!")
            return redirect('home123:feedback')  # ✅ Ensure correct URL namespace
        else:
            messages.error(request, "❌ Please correct the errors and try again.")

    return render(request, "feedback.html", {"form": form})

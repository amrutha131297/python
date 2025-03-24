from django.contrib import admin
from .models import Department
from .models import Doctor
from .models import PatientFeedback
from.models import Book


admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(PatientFeedback)
admin.site.register(Book)
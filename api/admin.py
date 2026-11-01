from django.contrib import admin

from .models import Appointment, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email")
    search_fields = ("last_name", "first_name", "email")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "student", "cancelled")
    list_filter = ("cancelled", "date")
    search_fields = (
        "student__last_name",
        "student__email",
        "comment",
    )

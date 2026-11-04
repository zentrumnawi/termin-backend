from django.contrib import admin
from django import forms
from django.db import models

from .models import Appointment, Shift, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email")
    search_fields = ("last_name", "first_name", "email")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "student", "tutor")
    list_filter = ("date", "tutor")
    search_fields = (
        "student__last_name",
        "student__email",
        "tutor__username",
        "comment",
    )
    formfield_overrides = {
        models.TimeField: {
            "widget": forms.TimeInput(format="%H:%M", attrs={"type": "time"})
        },
    }


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("date", "time", "tutor")
    list_filter = ("date", "tutor")
    search_fields = ("tutor__username",)
    formfield_overrides = {
        models.TimeField: {
            "widget": forms.TimeInput(format="%H:%M", attrs={"type": "time"})
        },
    }

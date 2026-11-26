from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("appointment_date", "doctor", "patient", "status", "duration_minutes")
    list_filter = ("status", "appointment_date")
    search_fields = (
        "doctor__username",
        "doctor__last_name",
        "patient__username",
        "patient__last_name",
    )
    readonly_fields = ("created_at", "updated_at")

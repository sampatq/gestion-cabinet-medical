from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor, Patient, Specialty, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "license_number")
    search_fields = ("username", "first_name", "last_name", "license_number")

    def get_readonly_fields(self, request, obj=None):
        return ("license_number",) if obj else ()


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "national_id", "phone")
    search_fields = ("username", "first_name", "last_name", "national_id")

    def get_readonly_fields(self, request, obj=None):
        return ("national_id",) if obj else ()


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

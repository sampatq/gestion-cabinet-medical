from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """Project user model used as the parent of doctors and patients."""

    pass


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)],
    )

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"Dr. {self.get_full_name() or self.username}"


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r"^\d{8}$")],
    )
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r"^\d{8}$")],
    )
    birth_date = models.DateField()

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def clean(self):
        super().clean()
        if self.birth_date and self.birth_date >= timezone.localdate():
            raise ValidationError(
                {"birth_date": "La date de naissance doit être antérieure à aujourd'hui."}
            )

    def __str__(self):
        return self.get_full_name() or self.username


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(Doctor, related_name="specialties")

    def __str__(self):
        return self.name

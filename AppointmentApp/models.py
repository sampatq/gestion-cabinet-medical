from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Status(models.TextChoices):
    PENDING = "PENDING", "En attente"
    CONFIRMED = "CONFIRMED", "Confirmé"
    CANCELLED = "CANCELLED", "Annulé"


class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        upload_to="prescriptions/",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(
        "AccountApp.Doctor",
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        "AccountApp.Patient",
        on_delete=models.CASCADE,
        related_name="appointments",
    )

    def clean(self):
        super().clean()
        if not self.appointment_date:
            return

        date_changed = self._state.adding
        if not self._state.adding and self.pk:
            previous_date = type(self).objects.filter(pk=self.pk).values_list(
                "appointment_date", flat=True
            ).first()
            date_changed = previous_date is not None and self.appointment_date != previous_date

        if date_changed and self.appointment_date <= timezone.now():
            raise ValidationError(
                {"appointment_date": "La date du rendez-vous doit être dans le futur."}
            )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "appointment_date"],
                name="unique_doctor_appointment_datetime",
            ),
        ]
        ordering = ["appointment_date"]

    def __str__(self):
        return f"{self.patient} — {self.doctor} — {self.appointment_date:%Y-%m-%d %H:%M}"

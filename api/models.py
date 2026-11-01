from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    comment = models.TextField(blank=True)
    cancelled = models.BooleanField(default=False)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self) -> str:
        return f"{self.date} {self.time} - {self.student}"

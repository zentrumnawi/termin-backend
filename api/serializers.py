from django.db import transaction
from rest_framework import serializers

from .models import Appointment, Shift, Student


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ("id", "date", "time")


class AppointmentCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, max_length=150)
    last_name = serializers.CharField(write_only=True, max_length=150)
    email = serializers.EmailField(write_only=True)
    shift_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Appointment
        fields = (
            "id",
            "date",
            "time",
            "comment",
            "first_name",
            "last_name",
            "email",
            "shift_id",
        )
        read_only_fields = ("id", "date", "time")

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        student, _ = Student.objects.get_or_create(
            email=email,
            defaults={"first_name": first_name, "last_name": last_name},
        )
        shift_id = validated_data.pop("shift_id")
        with transaction.atomic():
            # get and set tutor
            try:
                shift = Shift.objects.select_for_update().get(id=shift_id)
            except Shift.DoesNotExist:
                raise serializers.ValidationError("Shift not found")
            tutor = shift.tutor
            appointment = Appointment.objects.create(
                student=student,
                tutor=tutor,
                date=shift.date,
                time=shift.time,
                **validated_data,
            )
            # delete shift
            shift.delete()

        return appointment

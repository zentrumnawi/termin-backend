from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Appointment, Shift
from .serializers import AppointmentCreateSerializer, ShiftSerializer


class ShiftListView(ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer

from rest_framework.generics import ListAPIView

from .models import Shift
from .serializers import ShiftSerializer


class ShiftListView(ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

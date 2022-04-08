from .models import HR
from rest_framework import viewsets
from .serializers import HRSerializer
from .permissions import HRAccessPolicy


class HRViewSet(viewsets.ModelViewSet):
    permission_classes = (HRAccessPolicy,)
    queryset = HR.objects.all()
    serializer_class = HRSerializer

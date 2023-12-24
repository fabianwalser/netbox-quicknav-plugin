from netbox.api.viewsets import NetBoxModelViewSet

from .serializers import QuicknavButtonSerializer
from .. import models


## ----------------------------------------------------------------------------------------
## QuicknavButtonViewSet
class QuicknavButtonViewSet(NetBoxModelViewSet):
    queryset = models.QuicknavButton.objects.prefetch_related('tags')
    serializer_class = QuicknavButtonSerializer

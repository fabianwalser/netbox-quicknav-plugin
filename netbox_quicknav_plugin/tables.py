import django_tables2 as tables
from netbox.tables import NetBoxTable

from .models import QuicknavButton


## ----------------------------------------------------------------------------------------
## QuicknavButtonTable
class QuicknavButtonTable(NetBoxTable):
    title = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = QuicknavButton
        fields = ('pk', 'id', 'title', 'order', 'style', 'icon', 'divider', 'link')
        default_columns = ('title', 'order', 'style', 'icon', 'divider', 'link')

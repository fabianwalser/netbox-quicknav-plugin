from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

from .models import QuicknavButton


## ----------------------------------------------------------------------------------------
## QuicknavButtonForm
class QuicknavButtonForm(NetBoxModelForm):
    class Meta:
        model = QuicknavButton
        fields = ('title', 'order', 'style', 'icon', 'divider', 'link')


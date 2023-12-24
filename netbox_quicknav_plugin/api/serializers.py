from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from rest_framework import serializers

from ..models import QuicknavButton


## ----------------------------------------------------------------------------------------
## NestedQuicknavButtonSerializer
class NestedQuicknavButtonSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_quicknav_plugin-api:quicknavbutton-detail'
    )

    class Meta:
        model = QuicknavButton
        fields = ('id', 'url', 'display', 'title')


## ----------------------------------------------------------------------------------------
## QuicknavButtonSerializer
class QuicknavButtonSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_quicknav_plugin-api:quicknavbutton-detail'
    )

    class Meta:
        model = QuicknavButton
        fields = ('id', 'url', 'display', 'title', 'order', 'style', 'icon', 'divider', 'link', 'custom_fields', 'created', 'last_updated')

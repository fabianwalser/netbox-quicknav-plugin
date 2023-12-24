from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netbox_quicknav_plugin'

router = NetBoxRouter()
router.register('quicknav-buttons', views.QuicknavButtonViewSet)

urlpatterns = router.urls

from netbox.views import generic

from . import forms, models, tables


#
# Quicknav Button
#

## ----------------------------------------------------------------------------------------
## QuicknavButtonView
class QuicknavButtonView(generic.ObjectView):
    queryset = models.QuicknavButton.objects.all()


## ----------------------------------------------------------------------------------------
## QuicknavButtonListView
class QuicknavButtonListView(generic.ObjectListView):
    queryset = models.QuicknavButton.objects.all()
    table = tables.QuicknavButtonTable


## ----------------------------------------------------------------------------------------
## QuicknavButtonEditView
class QuicknavButtonEditView(generic.ObjectEditView):
    queryset = models.QuicknavButton.objects.all()
    form = forms.QuicknavButtonForm


## ----------------------------------------------------------------------------------------
## QuicknavButtonDeleteView
class QuicknavButtonDeleteView(generic.ObjectDeleteView):
    queryset = models.QuicknavButton.objects.all()

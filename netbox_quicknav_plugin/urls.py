from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (

    ## ----------------------------------------------------------------------------------------
    ## Quicknav Buttons
    path('quicknav/buttons/', views.QuicknavButtonListView.as_view(), name='quicknavbutton_list'),
    path('quicknav/buttons/add/', views.QuicknavButtonEditView.as_view(), name='quicknavbutton_add'),
    path('quicknav/buttons/<int:pk>/', views.QuicknavButtonView.as_view(), name='quicknavbutton'),
    path('quicknav/buttons/<int:pk>/edit/', views.QuicknavButtonEditView.as_view(), name='quicknavbutton_edit'),
    path('quicknav/buttons/<int:pk>/delete/', views.QuicknavButtonDeleteView.as_view(), name='quicknavbutton_delete'),
    path('quicknav/buttons/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='quicknavbutton_changelog', kwargs={
        'model': models.QuicknavButton
    }),

)

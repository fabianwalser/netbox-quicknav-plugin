from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (

    ## ----------------------------------------------------------------------------------------
    ## Quicknav Buttons
    path('buttons/', views.QuicknavButtonListView.as_view(), name='quicknavbutton_list'),
    path('buttons/add/', views.QuicknavButtonEditView.as_view(), name='quicknavbutton_add'),
    path('buttons/<int:pk>/', views.QuicknavButtonView.as_view(), name='quicknavbutton'),
    path('buttons/<int:pk>/edit/', views.QuicknavButtonEditView.as_view(), name='quicknavbutton_edit'),
    path('buttons/<int:pk>/delete/', views.QuicknavButtonDeleteView.as_view(), name='quicknavbutton_delete'),
    path('buttons/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='quicknavbutton_changelog', kwargs={
        'model': models.QuicknavButton
    }),

)

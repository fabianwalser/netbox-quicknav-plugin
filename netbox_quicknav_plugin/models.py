from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


## ----------------------------------------------------------------------------------------
## StyleChoices
class StyleChoices(ChoiceSet):
    key = 'QuicknavButton.style'

    CHOICES = [
        ('icon', 'Icon only'),
        ('text', 'Text only'),
        ('both', 'Icon and Text'),
    ]


## ----------------------------------------------------------------------------------------
## QuicknavButton
class QuicknavButton(NetBoxModel):
    title = models.CharField(
        max_length=100
    )
    order = models.PositiveIntegerField(
        default=0
    )
    style = models.CharField(
        max_length=10,
        choices=StyleChoices
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None,
        help_text='E.g: MDI Webfont from https://pictogrammers.com/library/mdi/',
    )
    divider = models.BooleanField(
        default=False
    )
    link = models.CharField(
        max_length=250,
        default='#',
    )

    class Meta:
        ordering = ('order', 'title')
        unique_together = ('order', 'title')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_quicknav_plugin:quicknavbutton', args=[self.pk])

from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

settings_menu = (
    PluginMenuItem(
        link='plugins:netbox_quicknav_plugin:quicknavbutton_list',
        link_text='Buttons',
        buttons=[
            PluginMenuButton(
                link='plugins:netbox_quicknav_plugin:quicknavbutton_add',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN
            )
        ]
    ),
)

menu = PluginMenu(
    label=f'Quicknav',
    groups=(
        ('Settings', settings_menu),
    ),
    icon_class='mdi mdi-link-box-outline'
)

from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

# compatibility with netbox v3.3 that does not have PluginMenu
try:
    from extras.plugins import PluginMenu

    HAVE_MENU = True
except ImportError:
    HAVE_MENU = False
    PluginMenu = PluginMenuItem

quicknavbutton_buttons = [
    PluginMenuButton(
        link='plugins:netbox_quicknav_plugin:quicknavbutton_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

settings_menu = (
    PluginMenuItem(
        link='plugins:netbox_quicknav_plugin:quicknavbutton_list',
        link_text='Buttons',
        permissions=["netbox_quicknav_plugin.view_quicknavbutton"],
        buttons=quicknavbutton_buttons,
    ),
)

if (HAVE_MENU):
    menu = PluginMenu(
        label=f'Quicknav',
        groups=(
            ('Settings', settings_menu),
        ),
        icon_class='mdi mdi-link-box-outline'
    )
else:
    # display under plugins
    menu_items = settings_menu

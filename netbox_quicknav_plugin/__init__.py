from extras.plugins import PluginConfig


class NetBoxQuicknavPluginConfig(PluginConfig):
    name = 'netbox_quicknav_plugin'
    verbose_name = 'NetBox Quicknav Plugin'
    description = 'Quicknav Plugin for NetBox'
    author = 'Fabian Walser'
    author_email = 'f.walser@dresohn.ch'
    version = '1.1.4'
    base_url = 'quicknav'


config = NetBoxQuicknavPluginConfig

from mcdreforged.api.all import *
from smptoolkit import commands

def on_load(server: PluginServerInterface, prev_module):
    commands.register_commands(server)

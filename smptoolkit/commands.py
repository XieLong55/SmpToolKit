from mcdreforged.api.all import *

def register_commands(server: PluginServerInterface):
    # 注册帮助信息
    server.register_help_message('!tp <target>', '传送至目标玩家')
    server.register_help_message('!kill / !suicide', '使自己自杀')

    # !tp <target> -> /tp <source> <target>
    server.register_command(
        Literal('!tp')
        .requires(lambda src: src.is_player)
        .then(
            Text('target')
            .suggests(lambda: server.get_player_list())
            .runs(lambda src, ctx: server.execute(f'tp {src.player} {ctx["target"]}'))
        )
    )

    # !kill / !suicide -> /kill <source>
    kill_node = Literal('!kill').requires(lambda src: src.is_player).runs(
        lambda src: server.execute(f'kill {src.player}')
    )
    suicide_node = Literal('!suicide').requires(lambda src: src.is_player).runs(
        lambda src: server.execute(f'kill {src.player}')
    )

    server.register_command(kill_node)
    server.register_command(suicide_node)

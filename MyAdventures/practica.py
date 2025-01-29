import mcpi.minecraft as game
import framework.bot_manager as BotManager
import bots.tnt_bot as TNT
import bots.chat_bot as ChatBOT
import bots.insult_bot as Insult

# Instanciar el BotManager Singleton
bot_manager = BotManager.bot_manager.getInstance()
print(bot_manager)

mc = game.Minecraft.create()    # Connect to the Minecraft game
Script = 1  # Control variable to exit program when finished

# Función para detener los bots
def stop_bot(bot):
    bot.stop()

# Funcion para activar bots
def enableBot(player, bot_type):
    bot_manager.get_bot_list(bot_type)[player].begin()

# Funcion para desactivar bots
def disableBot(player, bot_type):
    bot_list = bot_manager.get_bot_list(bot_type)
    bot_list[player].stop()
    del bot_list[player]
    if bot_type == 'TNT'.casefold():
        bot_list[player] = TNT(player)
    elif bot_type == 'ChatBOT'.casefold():
        bot_list[player] = ChatBOT(player)
    elif bot_type == 'Insult'.casefold():
        bot_list[player] = Insult(player)


# Actualización inicial
bot_manager.printLists()
bot_manager.update_player_list(mc)
bot_manager.printLists()


mc.postToChat("§a<MAIN> Main program is running!!")

# Diccionario para comandos y funciones correspondientes
command_map = {
    ":enableTNT": lambda player: enableBot(player, 'TNT'),
    ":disableTNT": lambda player: disableBot(player, 'TNT'),
    ":enableGPT": lambda player: enableBot(player, 'chatBOT'),
    ":disableGPT": lambda player: disableBot(player, 'chatBOT'),
    ":enableInsult": lambda player: enableBot(player, 'Insult'),
    ":disableInsult": lambda player: disableBot(player, 'Insult'),
    ":endProgram": None  # Control especial para terminar el script
}

# Bucle principal
while Script:
    bot_manager.update_player_list(mc)
    
    # Leer eventos de chat
    chatEvents = mc.events.pollChatPosts()

    for command in chatEvents:
        text = str(command.message).casefold()  # Convierte una vez a minúsculas
        if not text.startswith(":"):
            continue

        player = command.entityId

        # Ejecutar comando si está en el mapa
        if text in command_map:
            action = command_map[text]
            if action:
                action(player)
            else:  # Comando especial ":endProgram"
                for bot_type in ['tnt', 'chatbot', 'insult']:
                    bot_list = bot_manager.get_bot_list(bot_type)
                    for bot in bot_list.values():
                        stop_bot(bot)
                Script = 0  # Salir del bucle principal


mc.postToChat("§a<MAIN> ***Ended execution of main program!!")
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
        bot_list[player] = TNT
    elif bot_type == 'ChatBOT'.casefold():
        bot_list[player] = ChatBOT
    elif bot_type == 'Insult'.casefold():
        bot_list[player] = Insult


# Actualización inicial
bot_manager.printLists()
bot_manager.update_player_list(mc)
bot_manager.printLists()


mc.postToChat("§a<MAIN> Main program is running!!")

# Bucle principal
while(Script):
    bot_manager.update_player_list(mc)
    
    # Read chat to see if anyone used a custom command
    chatEvents = mc.events.pollChatPosts()
    
    for command in chatEvents:  
        text = str(command.message) # Convert chat event to str
        if(not text.startswith(":")):   # Skip if it doesn't start with ":"
            continue
        
        player = command.entityId   # Else, register what player sent the command
        
        # Check what command was executed (ignore case)
        if (text.casefold() == ":enableTNT".casefold()):
            enableBot(player, 'TNT'.casefold())
            
        elif (text.casefold() == ":disableTNT".casefold()):
            disableBot(player, 'TNT'.casefold())
            
        elif (text.casefold() == ":enableGPT".casefold()):
            enableBot(player, 'ChatBOT'.casefold())
            
        elif (text.casefold() == ":disableGPT".casefold()):
            disableBot(player, 'ChatBOT'.casefold())

        elif (text.casefold() == ":enableInsult".casefold()):
            enableBot(player, 'Insult'.casefold())
            
        elif (text.casefold() == ":disableInsult".casefold()):
            disableBot(player, 'Insult'.casefold())
            
        elif (text.casefold() == ":endProgram".casefold()):
            mc.postToChat("§a<MAIN> Main program finished!!")
            # Detener todos los bots y terminar el programa
            for bot_type in ['TNT'.casefold(), 'ChatBOT'.casefold(), 'Insult'.casefold()]:
                bot_list = bot_manager.get_bot_list(bot_type)
                list(map(stop_bot, bot_list.values()))
                
            Script = 0  # Command to finish the execution of this program


mc.postToChat("§a<MAIN> Program stopped")
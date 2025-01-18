import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from mcpi.minecraft import Minecraft
from practicaTAP.framework.event_system import EventSystem
from practicaTAP.bots.insult_bot import InsultBot
from practicaTAP.bots.tnt_bot import TNTBot
from practicaTAP.bots.chat_bot import ChatBot


def main_loop(event_system):
    mc = Minecraft.create()
    
    while True:
        chat_messages = mc.events.pollChatPosts()
        if chat_messages:
            event_system.publish_event("chat_event", chat_messages)
            
        time.sleep(0.1)
        
if __name__  == "_main_":
    #Create the event system
    event_system = EventSystem()
    
    #Initialize the bot
    insult_bot = InsultBot()
    chat_bot = ChatBot()
    tnt_bot = TNTBot()
    
    #Set the event system
    insult_bot.event_system = event_system
    chat_bot.event_system = event_system
    tnt_bot.event_system = event_system
    
    #Register the bots for chats
    event_system.register_event("chat_event", insult_bot.on_chat)
    event_system.register_event("chat_event", chat_bot.on_chat)
    event_system.register_event("chat_event", tnt_bot.on_chat)
    
    #Run the main loop
    main_loop(event_system)
    
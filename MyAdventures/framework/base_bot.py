import mcpi.minecraft as game
from threading import Thread

# Clase base abstracta para un bot
class Bot():
    def __init__(self, entity):
        self.mc = game.Minecraft.create()  # Conexión al servidor de Minecraft
        self.entity = entity  # Jugador que llamó a la función
        self.control = None  # Variable de control para el bucle principal de la función del bot
        self.t1 = Thread  # Declaración de un hilo para el bot (debe ser actualizado por el bot específico)
        self.player_name = self.mc.entity.getName(self.entity)
    
    # Función principal para iniciar un hilo con el bot
    def begin(self):
        if not self.t1.is_alive():
            self.control = True
            self.t1.start()
            self.mc.postToChat(f"§2<{self.name}> El bot ha sido habilitado para {self.player_name}!")
        else:
            self.mc.postToChat(f"§2<{self.name}> El bot ya se está ejecutando para {self.player_name}!")

    # Función principal para detener el hilo del bot
    def stop(self):
        if self.t1.is_alive():
            self.control = False
            self.t1.join()
            self.mc.postToChat(f"§2<{self.name}> El bot ha sido deshabilitado para {self.player_name}!")
        else:
            self.mc.postToChat(f"§2<{self.name}> El bot no se está ejecutando aún para {self.player_name}!")

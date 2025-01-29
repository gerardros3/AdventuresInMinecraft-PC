import random
import time
import mcpi.entity as entities
from threading import Thread
from framework.base_bot import Bot
import math

# Clase específica del bot para generar TNT cerca del jugador
class TNT(Bot):
    def __init__(self, entity):
        super().__init__(entity)  # Heredar atributos de la clase base
        self.name = "TNTBot"  # Nombre de este bot específico
        self.t1 = Thread(target=self._main)  # Actualizar el hilo con la función a ejecutar
        self.counter = 0  # Contador para controlar los intervalos de generación de TNT

    # Función para generar TNT en un círculo alrededor del jugador
    def spawn_tnt_circle(self, pos, radius=5, num_tnt=10):
        """
        Genera un círculo de TNT alrededor del jugador.
        :param pos: posición central del jugador
        :param radius: radio del círculo
        :param num_tnt: cantidad de TNT en el círculo
        """
        angle_increment = 2 * math.pi / num_tnt  # Incremento angular para distribuir los TNT
        
        for i in range(num_tnt):
            angle = i * angle_increment
            # Calcular las coordenadas X y Z para cada TNT
            x = pos.x + int(radius * math.cos(angle))
            z = pos.z + int(radius * math.sin(angle))
            y = pos.y + 2  # Mantenerlo 2 bloques por encima del jugador
            # Generar TNT en la posición calculada
            self.mc.spawnEntity(x, y, z, entities.PRIMED_TNT.id)

    # Función específica del bot TNT
    def _main(self):
        while self.control:  # Ejecutar mientras el bot esté habilitado
            if self.counter > 0:
                time.sleep(1)  # Esperar 1 segundo
                self.counter -= 1  # Decrementar el contador
            else:
                self.counter = random.randint(1, 5)  # Intervalo aleatorio entre 1 y 5 segundos
                pos = self.mc.entity.getTilePos(self.entity) 

                # Generar un círculo de TNT alrededor del jugador
                self.spawn_tnt_circle(pos, radius=5, num_tnt=8) 

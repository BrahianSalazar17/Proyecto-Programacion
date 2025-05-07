from datetime import datetime, timedelta
#========Clase Cliente========
class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.membresia = None
    def asignar_membresia(self, membresia):
        self.membresia = membresia
    def consultar_estado_membresia(self):
        if self.membresia:
            self.membresia.verificar_vencimiento()
            return f"Membresía: {self.membresia.tipo}, Estado: {self.membresia.estado}"
        return "Sin membresía"

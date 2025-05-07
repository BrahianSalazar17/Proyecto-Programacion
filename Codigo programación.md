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
        # ===== Clase Membresía =====
class Membresia:
    def __init__(self, tipo, costo, duracion_dias):
        self.tipo = tipo
        self.costo = costo
        self.fecha_inicio = datetime.now()
        self.fecha_fin = self.fecha_inicio + timedelta(days=duracion_dias)
        self.estado = "Activa"
    def verificar_vencimiento(self):
        if datetime.now() > self.fecha_fin:
            self.estado = "Vencida"

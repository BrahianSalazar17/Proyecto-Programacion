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
# ===== Clase Registro de Pagos =====
class RegistroPagos:
    def __init__(self, cliente, monto, metodo_pago):
        self.cliente = cliente
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha_pago = datetime.now()
    def mostrar_pago(self):
        print(f"{self.cliente.nombre} pagó ${self.monto} por {self.metodo_pago} el {self.fecha_pago.date()}")
        
# ===== Clase Registro de Entrada =====
class RegistroEntrada:
    def __init__(self, cliente):
        self.cliente = cliente
        self.fecha = datetime.now()
    def validar_acceso(self):
        if self.cliente.membresia and self.cliente.membresia.estado == "Activa":
            print(f"Acceso permitido para {self.cliente.nombre}")
        else:
            print(f"Acceso denegado para {self.cliente.nombre}")

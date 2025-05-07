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
            # ===== Datos Simulados =====
clientes = []

# ===== Funciones del sistema =====
def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    cliente = Cliente(len(clientes)+1, nombre)
    clientes.append(cliente)
    print(f"Cliente registrado con ID: {cliente.id_cliente}")

def activar_membresia():
    id_cliente = int(input("ID cliente: "))
    tipo = input("Tipo: ")
    costo = float(input("Costo: "))
    dias = int(input("Duración en días: "))
    membresia = Membresia(tipo, costo, dias)
    clientes[id_cliente - 1].asignar_membresia(membresia)
    print("Membresía activada.")

def registrar_pago()
id_cliente = int(input("ID cliente:"))
monto = float(input("Monto"))
metodo = input ("Metodo de pago")
pago = RegistreoPagos(clientes[id_cliente - 1], monto, metodo)
    pago.mostrar_pago()
def validar_entrada():
id_cliente = int(input("ID cliente"))
entrada =RegistroEntrada(clientes[id_cliente - 1])
    entrada.validar_acceso()
def consultar_membresia():
id_cliente = int(input("ID cliente:"))
print(clientes[id_cliente - 1].consultar_estado_membresia()]
# ===== Menú principal =====
def menu():
    while True:
      print("\n--- SISTEMA DE GIMNASIO ---")
        print("1. Registrar cliente")
        print("2. Activar membresía")
        print("3. Registrar pago")
        print("4. Validar acceso al gimnasio")
        print("5. Consultar membresía")
        print("6. Salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            activar_membresia()
        elif opcion == "3":
            registrar_pago()
        elif opcion == "4":
            validar_entrada()
        elif opcion == "5":
            consultar_membresia()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
      
        
        


    



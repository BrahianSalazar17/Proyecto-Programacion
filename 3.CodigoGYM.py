from datetime import datetime, timedelta

# ===== Clase Cliente =====
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

# ===== Clase Membresía (Base) =====
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

# ===== Subclases con polimorfismo =====
class MembresiaBasica(Membresia):
    def verificar_vencimiento(self):
        super().verificar_vencimiento()
        if self.estado == "Vencida":
            print("Su membresía básica ha vencido.")

class MembresiaPremium(Membresia):
    def verificar_vencimiento(self):
        super().verificar_vencimiento()
        if self.estado == "Vencida":
            print("Su membresía premium ha vencido, considere renovarla para más beneficios.")

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

# ===== Base de datos simulada =====
clientes = {}

# ===== Funciones del sistema =====
def registrar_cliente():
    id_cliente = int(input("ID del cliente: "))
    if id_cliente in clientes:
        print("Este ID ya está registrado.")
        return
    nombre = input("Nombre del cliente: ")
    cliente = Cliente(id_cliente, nombre)
    clientes[id_cliente] = cliente
    print(f"Cliente registrado con ID: {cliente.id_cliente}")

def activar_membresia():
    id_cliente = int(input("ID cliente: "))
    if id_cliente not in clientes:
        print("Cliente no encontrado.")
        return

    tipo = input("Tipo (Basica / Premium / Otra): ").strip()
    costo = float(input("Costo: "))
    dias = int(input("Duración en días: "))

    if tipo.lower() == "basica":
        membresia = MembresiaBasica(tipo, costo, dias)
    elif tipo.lower() == "premium":
        membresia = MembresiaPremium(tipo, costo, dias)
    else:
        membresia = Membresia(tipo, costo, dias)

    clientes[id_cliente].asignar_membresia(membresia)
    print("Membresía activada.")

def registrar_pago():
    id_cliente = int(input("ID cliente: "))
    if id_cliente not in clientes:
        print("Cliente no encontrado.")
        return
    monto = float(input("Monto: "))
    metodo = input("Método de pago: ")
    pago = RegistroPagos(clientes[id_cliente], monto, metodo)
    pago.mostrar_pago()

def validar_entrada():
    id_cliente = int(input("ID cliente: "))
    if id_cliente not in clientes:
        print("Cliente no encontrado.")
        return
    entrada = RegistroEntrada(clientes[id_cliente])
    entrada.validar_acceso()

def consultar_membresia():
    id_cliente = int(input("ID cliente: "))
    if id_cliente not in clientes:
        print("Cliente no encontrado.")
        return
    print(clientes[id_cliente].consultar_estado_membresia())

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

# Clases principales del sistema HelpDesk EDU


class Usuario:

    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email} - {self.rol}"


class Ticket:

    estados_validos = [
        "Open",
        "In Progress",
        "Resolved",
        "Closed",
        "Cancelled"
    ]

    def __init__(
        self,
        id,
        titulo,
        categoria,
        prioridad,
        solicitante,
        tecnico=None
    ):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = tecnico
        self._status = "Open"

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in self.estados_validos:
            print("Error: estado no permitido.")
            return False

        self._status = nuevo_estado
        return True

    def asignar_tecnico(self, tecnico):
        if tecnico.rol != "technician":
            print("Error: el usuario no tiene rol de technician.")
            return False

        self.tecnico = tecnico
        return True

    def __str__(self):
        tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"

        return (
            f"Ticket #{self.id} | "
            f"{self.titulo} | "
            f"{self.categoria} | "
            f"{self.prioridad} | "
            f"Estado: {self._status} | "
            f"Solicitante: {self.solicitante.nombre} | "
            f"Técnico: {tecnico}"
        )


# Creamos dos usuarios
solicitante = Usuario(
    1,
    "Luis Morales",
    "luis@umg.edu.gt",
    "requester"
)

tecnico = Usuario(
    2,
    "Carlos Perez",
    "carlos@umg.edu.gt",
    "technician"
)

# Creamos tres tickets
ticket1 = Ticket(
    101,
    "Computadora no enciende",
    "Hardware",
    "High",
    solicitante
)

ticket2 = Ticket(
    102,
    "No hay conexión",
    "Network",
    "Medium",
    solicitante
)

ticket3 = Ticket(
    103,
    "Error en programa",
    "Software",
    "Low",
    solicitante
)

tickets = [ticket1, ticket2, ticket3]

# Mostramos los tickets
print("=== TICKETS INICIALES ===")

for ticket in tickets:
    print(ticket)

# Asignamos el técnico al primer ticket
print("\n=== ASIGNACIÓN DE TÉCNICO ===")

if ticket1.asignar_tecnico(tecnico):
    print("Técnico asignado correctamente.")

# Cambiamos el estado
print("\n=== CAMBIO DE ESTADO ===")

if ticket1.cambiar_estado("In Progress"):
    print("El ticket pasó a In Progress.")

# Probamos un estado que no está permitido
print("\n=== PRUEBA DE ESTADO NO VÁLIDO ===")

ticket1.cambiar_estado("Pendiente")

print("\n=== TICKET ACTUALIZADO ===")
print(ticket1)
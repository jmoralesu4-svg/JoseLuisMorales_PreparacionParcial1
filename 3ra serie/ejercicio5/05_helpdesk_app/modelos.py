# Clases principales de la mini aplicación HelpDesk


class Usuario:

    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.rol}"


class Ticket:

    estados_validos = [
        "Open",
        "In Progress",
        "Resolved",
        "Closed",
        "Cancelled"
    ]

    def __init__(self, id, titulo, categoria, prioridad, solicitante):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self.status = "Open"

    def __str__(self):
        tecnico = self.tecnico.nombre if self.tecnico else "Sin asignar"

        return (
            f"#{self.id} | {self.titulo} | "
            f"{self.categoria} | {self.prioridad} | "
            f"{self.status} | Técnico: {tecnico}"
        )
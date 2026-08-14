# Funciones que manejan las operaciones de los tickets

from modelos import Ticket


def registrar_ticket(tickets, ticket):
    tickets.append(ticket)
    return ticket


def listar_tickets(tickets):
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    for ticket in tickets:
        print(ticket)


def buscar_ticket(tickets, id_ticket):
    for ticket in tickets:
        if ticket.id == id_ticket:
            return ticket

    return None


def asignar_tecnico(tickets, id_ticket, tecnico):
    ticket = buscar_ticket(tickets, id_ticket)

    if ticket is None:
        print("Error: ticket no encontrado.")
        return False

    if tecnico.rol != "technician":
        print("Error: el usuario no es técnico.")
        return False

    ticket.tecnico = tecnico
    print("Técnico asignado correctamente.")
    return True


def cambiar_estado(tickets, id_ticket, nuevo_estado):
    ticket = buscar_ticket(tickets, id_ticket)

    if ticket is None:
        print("Error: ticket no encontrado.")
        return False

    if nuevo_estado not in Ticket.estados_validos:
        print("Error: estado no válido.")
        return False

    ticket.status = nuevo_estado
    print(f"Estado cambiado a {nuevo_estado}.")
    return True
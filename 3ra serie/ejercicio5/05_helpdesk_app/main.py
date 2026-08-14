# Punto de entrada de la mini aplicación HelpDesk

from modelos import Usuario, Ticket
from servicios import (
    registrar_ticket,
    listar_tickets,
    buscar_ticket,
    asignar_tecnico,
    cambiar_estado
)


def main():
    tickets = []

    # Creamos un solicitante y un técnico
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

    while True:
        print("\n=== HELPDESK EDU ===")
        print("1. Registrar ticket")
        print("2. Listar tickets")
        print("3. Buscar ticket")
        print("4. Asignar técnico")
        print("5. Cambiar estado")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                id_ticket = int(input("ID del ticket: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            titulo = input("Título: ").strip()
            categoria = input("Categoría: ").strip()
            prioridad = input("Prioridad: ").strip()

            ticket = Ticket(
                id_ticket,
                titulo,
                categoria,
                prioridad,
                solicitante
            )

            registrar_ticket(tickets, ticket)
            print("Ticket registrado correctamente.")

        elif opcion == "2":
            listar_tickets(tickets)

        elif opcion == "3":
            try:
                id_ticket = int(input("ID a buscar: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            ticket = buscar_ticket(tickets, id_ticket)

            if ticket:
                print(ticket)
            else:
                print("Ticket no encontrado.")

        elif opcion == "4":
            try:
                id_ticket = int(input("ID del ticket: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            asignar_tecnico(tickets, id_ticket, tecnico)

        elif opcion == "5":
            try:
                id_ticket = int(input("ID del ticket: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            nuevo_estado = input(
                "Nuevo estado (Open/In Progress/Resolved/Closed/Cancelled): "
            ).strip()

            cambiar_estado(tickets, id_ticket, nuevo_estado)

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
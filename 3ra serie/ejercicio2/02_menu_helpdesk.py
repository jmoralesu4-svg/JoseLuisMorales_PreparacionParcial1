# Menú modular para administrar tickets en memoria

tickets = []


def pedir_opcion():
    print("\n=== HELPDESK EDU ===")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")

    return input("Seleccione una opción: ").strip()


def registrar_ticket():
    print("\n=== REGISTRAR TICKET ===")

    try:
        numero = int(input("Número de ticket: "))
    except ValueError:
        print("Error: el número debe ser entero.")
        return

    solicitante = input("Solicitante: ").strip()
    titulo = input("Título: ").strip()
    prioridad = input("Prioridad (Low/Medium/High/Critical): ").strip()

    if not solicitante or not titulo or not prioridad:
        print("Error: no se permiten campos vacíos.")
        return

    ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "prioridad": prioridad,
        "status": "Open"
    }

    tickets.append(ticket)
    print("Ticket registrado correctamente.")


def listar_tickets():
    print("\n=== TICKETS REGISTRADOS ===")

    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    for ticket in tickets:
        print(
            f"#{ticket['numero']} | "
            f"{ticket['solicitante']} | "
            f"{ticket['titulo']} | "
            f"{ticket['prioridad']} | "
            f"{ticket['status']}"
        )


def buscar_por_solicitante():
    nombre = input("Ingrese el nombre del solicitante: ").strip().lower()

    encontrados = 0

    for ticket in tickets:
        if ticket["solicitante"].lower() == nombre:
            print(
                f"Ticket #{ticket['numero']} - "
                f"{ticket['titulo']} - "
                f"{ticket['prioridad']}"
            )
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron tickets para ese solicitante.")


def mostrar_resumen():
    print("\n=== RESUMEN POR PRIORIDAD ===")

    prioridades = ["Low", "Medium", "High", "Critical"]

    for prioridad in prioridades:
        cantidad = 0

        for ticket in tickets:
            if ticket["prioridad"].lower() == prioridad.lower():
                cantidad += 1

        print(f"{prioridad}: {cantidad}")


def ejecutar_menu():
    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket()

        elif opcion == "2":
            listar_tickets()

        elif opcion == "3":
            buscar_por_solicitante()

        elif opcion == "4":
            mostrar_resumen()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_menu()
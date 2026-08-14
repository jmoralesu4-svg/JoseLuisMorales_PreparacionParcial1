# Registro de un ticket de HelpDesk

print("=== REGISTRO DE TICKET ===")

# Pedimos el número y comprobamos que sea entero
try:
    numero = int(input("Número de ticket: "))
except ValueError:
    print("Error: el número de ticket debe ser un entero.")
    exit()

solicitante = input("Solicitante: ").strip()
titulo = input("Título: ").strip()
descripcion = input("Descripción: ").strip()

# Comprobamos que los campos obligatorios no estén vacíos
if not solicitante or not titulo or not descripcion:
    print("Error: los campos obligatorios no pueden estar vacíos.")
    exit()

print("\nCategorías: General, Hardware, Software, Network")
categoria = input("Categoría: ").strip()

print("\nPrioridades: Low, Medium, High, Critical")
prioridad = input("Prioridad: ").strip()

categorias_validas = ["general", "hardware", "software", "network"]
prioridades_validas = ["low", "medium", "high", "critical"]

# Validamos la categoría sin importar mayúsculas o minúsculas
if categoria.lower() not in categorias_validas:
    print("Error: categoría no válida.")
    exit()

# Validamos la prioridad
if prioridad.lower() not in prioridades_validas:
    print("Error: prioridad no válida.")
    exit()

categoria = categoria.title()
prioridad = prioridad.title()

# Guardamos la información en un diccionario
ticket = {
    "numero": numero,
    "solicitante": solicitante,
    "titulo": titulo,
    "descripcion": descripcion,
    "categoria": categoria,
    "prioridad": prioridad,
    "status": "Open"
}

# Mostramos el resumen final
print("\n=== TICKET REGISTRADO ===")
print(f"Número: {ticket['numero']}")
print(f"Solicitante: {ticket['solicitante']}")
print(f"Título: {ticket['titulo']}")
print(f"Descripción: {ticket['descripcion']}")
print(f"Categoría: {ticket['categoria']}")
print(f"Prioridad: {ticket['prioridad']}")
print(f"Estado: {ticket['status']}")
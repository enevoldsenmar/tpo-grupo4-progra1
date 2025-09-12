#SISTEMA GESTION DE BIBLIOTECAS GRUPO 4 VIERNES TARDE

# ---- Funciones ----
def mostrar_menu():
    print("\n--- Biblioteca ---")
    print("1. Mostrar libros")
    print("2. Registrar usuario")
    print("3. Mostrar usuarios")
    print("0. Salir")

def mostrar_libros(matriz_libros):
    print("\n--- Lista de Libros ---")
    print("ID | Título                | Autor              | Disponible")
    for fila in matriz_libros:
        print(f"{fila[0]:<3}| {fila[1]:<20}| {fila[2]:<18}| {fila[3]}")

def registrar_usuario(usuarios):
    nombre = input("Ingrese nombre del usuario: ")
    usuarios.append(nombre)
    print("Usuario registrado con éxito.")

def mostrar_usuarios(usuarios):
    print("\n--- Lista de Usuarios ---")
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for i, usuario in enumerate(usuarios):
            print(f"{i+1}. {usuario}")


#Programa Principal
libros = [
    [1, "El Quijote", "Cervantes", "Sí"], #ID, Titulo, Autor, Disponibilidad
    [2, "Cien Años de Soledad", "G. García Márquez", "Sí"],
    [3, "La Odisea", "Homero", "Sí"]
]

usuarios = []       # lista de usuarios

opcion = -1
while opcion != 0:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_libros(libros)
    elif opcion == 2:
        registrar_usuario(usuarios)
    elif opcion == 3:
        mostrar_usuarios(usuarios)
    elif opcion == 0:
        print("Saliendo del sistema...")
    else:
        print("Opción inválida, intente nuevamente.")



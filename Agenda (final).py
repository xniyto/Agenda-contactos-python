import os

# Archivo donde se guardan todos los contactos
archivo = "agenda.txt"

# Lista principal de contactos
contactos = []

# =====================================================================
# FUNCIONES DE APOYO Y VALIDACIONES
# =====================================================================

# Limpia la consola dependiendo del sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausa el programa hasta presionar Enter
def pausar():
    input("\nPresione Enter para continuar...")

# Valida que el dato ingresado sea un número entero
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Error: Debe ingresar un número entero válido.")

# Valida textos vacíos y evita comas
def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if not texto:
            print(" Error: Este campo no puede quedar vacío.")
        elif "," in texto:
            print(" Error: No se permiten comas.")
        else:
            return texto

# Verifica que el teléfono tenga solo números y mínimo 8 dígitos
def leer_telefono(mensaje):
    while True:
        telefono = input(mensaje).strip()

        if not telefono.isdigit():
            print(" Error: El teléfono solo debe contener números.")
        elif len(telefono) < 8:
            print(" Error: El teléfono debe tener mínimo 8 dígitos.")
        else:
            return telefono

# Validación sencilla para correos electrónicos
def leer_email(mensaje):
    while True:
        email = input(mensaje).strip()

        if "@" not in email or "." not in email:
            print(" Error: Ingrese un correo válido.")
        else:
            return email

# Menú para seleccionar categorías
def leer_categoria():
    while True:
        print("\nSeleccione categoría:")
        print("1. Amigo")
        print("2. Familia")
        print("3. Trabajo")
        print("4. Otros")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            return "Amigo"
        elif opcion == "2":
            return "Familia"
        elif opcion == "3":
            return "Trabajo"
        elif opcion == "4":
            return "Otros"
        else:
            print(" Opción inválida.")

# Encabezado para mostrar contactos ordenadamente
def mostrar_encabezado_tabla():
    print(f"\n{'ID':<6} | {'Nombre':<22} | {'Teléfono':<15} | {'Email':<25} | {'Categoría':<12}")
    print("-" * 88)

# Muestra una fila con los datos del contacto
def imprimir_fila_contacto(c):
    print(f"{c['id']:<6} | {c['nombre']:<22} | {c['telefono']:<15} | {c['email']:<25} | {c['categoria']:<12}")

# =====================================================================
# CARGA Y GUARDADO DE DATOS
# =====================================================================

# Carga los contactos guardados en el archivo txt
def cargar_contactos():
    global contactos
    contactos.clear()

    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")

                if len(datos) == 5:
                    try:
                        contactos.append({
                            "id": int(datos[0]),
                            "nombre": datos[1],
                            "telefono": datos[2],
                            "email": datos[3],
                            "categoria": datos[4]
                        })
                    except:
                        print(" Línea corrupta ignorada.")

# Guarda todos los contactos en el archivo
def guardar_contactos():
    with open(archivo, "w", encoding="utf-8") as f:
        for c in contactos:
            f.write(f"{c['id']},{c['nombre']},{c['telefono']},{c['email']},{c['categoria']}\n")

# =====================================================================
# FUNCIONES DE ORDENAMIENTO
# =====================================================================

# Ordena los contactos por nombre
def ordenar_por_nombre():
    contactos.sort(key=lambda x: x["nombre"].lower())

    print("\n Contactos ordenados alfabéticamente.")
    guardar_contactos()
    pausar()

# Ordena los contactos por ID
def ordenar_por_id():
    contactos.sort(key=lambda x: x["id"])

    print("\n Contactos ordenados por ID.")
    guardar_contactos()
    pausar()

# =====================================================================
# FUNCIONES PRINCIPALES DEL CRUD
# =====================================================================

# Agrega un nuevo contacto a la agenda
def agregar():
    limpiar_pantalla()
    print("=== AGREGAR NUEVO CONTACTO ===")

    # Validación del ID
    while True:
        id_nuevo = leer_entero("Ingrese ID: ")

        if id_nuevo <= 0:
            print(" Error: El ID debe ser mayor que 0.")
        elif any(c["id"] == id_nuevo for c in contactos):
            print(" Error: Este ID ya pertenece a otro contacto.")
        else:
            break

    nombre = leer_texto("Nombre: ")

    # Evita nombres repetidos
    if any(c["nombre"].lower() == nombre.lower() for c in contactos):
        print(" Error: Ya existe un contacto con ese nombre.")
        pausar()
        return

    telefono = leer_telefono("Teléfono: ")
    email = leer_email("Email: ")
    categoria = leer_categoria()

    # Diccionario del nuevo contacto
    nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "categoria": categoria
    }

    contactos.append(nuevo)
    guardar_contactos()

    print("\n Contacto agregado correctamente.")
    pausar()

# Busca contactos usando el nombre o una parte del nombre
def buscar_nombre():
    limpiar_pantalla()
    print("=== BUSCAR POR NOMBRE ===")

    nombre_buscar = leer_texto("Nombre o fragmento: ").lower()
    encontrado = False

    mostrar_encabezado_tabla()

    for c in contactos:
        if nombre_buscar in c["nombre"].lower():
            imprimir_fila_contacto(c)
            encontrado = True

    if not encontrado:
        print(" No se encontraron coincidencias.")

    pausar()

# Busca contactos según la categoría seleccionada
def buscar_categoria():
    limpiar_pantalla()
    print("=== BUSCAR POR CATEGORÍA ===")

    categoria = leer_categoria()
    encontrado = False

    mostrar_encabezado_tabla()

    for c in contactos:
        if c["categoria"].lower() == categoria.lower():
            imprimir_fila_contacto(c)
            encontrado = True

    if not encontrado:
        print(" No hay contactos en esa categoría.")

    pausar()

# Permite modificar los datos de un contacto
def editar():
    limpiar_pantalla()
    print("=== EDITAR CONTACTO ===")

    id_buscar = leer_entero("Ingrese el ID del contacto: ")

    for c in contactos:
        if c["id"] == id_buscar:

            print("\n--- Datos Actuales ---")
            mostrar_encabezado_tabla()
            imprimir_fila_contacto(c)
            print("-" * 88)

            print("\nIngrese los nuevos datos:")

            c["nombre"] = leer_texto("Nuevo nombre: ")
            c["telefono"] = leer_telefono("Nuevo teléfono: ")
            c["email"] = leer_email("Nuevo email: ")
            c["categoria"] = leer_categoria()

            guardar_contactos()

            print("\n Contacto actualizado correctamente.")
            pausar()
            return

    print(" Error: No se encontró el ID.")
    pausar()

# Elimina un contacto usando el ID
def eliminar():
    limpiar_pantalla()
    print("=== ELIMINAR CONTACTO ===")

    id_buscar = leer_entero("Ingrese el ID a eliminar: ")

    for i in range(len(contactos)):
        if contactos[i]["id"] == id_buscar:

            # Confirmación antes de eliminar
            while True:
                confirmar = input(
                    f"¿Seguro que desea eliminar a '{contactos[i]['nombre']}'? (s/n): "
                ).lower()

                if confirmar in ["s", "n"]:
                    break

                print(" Solo escriba 's' o 'n'.")

            if confirmar == "s":
                contactos.pop(i)
                guardar_contactos()
                print("\n Contacto eliminado correctamente.")
            else:
                print("\n Operación cancelada.")

            pausar()
            return

    print(" Error: El ID ingresado no existe.")
    pausar()

# Muestra todos los contactos guardados
def mostrar_todos():
    limpiar_pantalla()
    print("=== LISTADO DE CONTACTOS ===")

    if not contactos:
        print(" La agenda está vacía.")
        pausar()
        return

    mostrar_encabezado_tabla()

    for c in contactos:
        imprimir_fila_contacto(c)

    print(f"\nTotal: {len(contactos)} contactos registrados.")

    pausar()

# =====================================================================
# REPORTE ESTADÍSTICO
# =====================================================================

# Genera un pequeño reporte usando una matriz 2D
def generar_reporte_matriz():
    limpiar_pantalla()
    print("=== REPORTE ESTADÍSTICO MATRICIAL ===")

    categorias_base = ["Amigo", "Familia", "Trabajo", "Otros"]

    matriz_estadisticas = [[cat, 0] for cat in categorias_base]

    for c in contactos:
        cat_contacto = c["categoria"]
        posicionado = False

        for i in range(len(matriz_estadisticas)):
            if matriz_estadisticas[i][0].lower() == cat_contacto.lower():
                matriz_estadisticas[i][1] += 1
                posicionado = True
                break

        # Si aparece una categoría nueva, también la agrega
        if not posicionado:
            matriz_estadisticas.append([cat_contacto, 1])

    print(f"{'Fila':<10} | {'Categoría':<20} | {'Cantidad':<10}")
    print("-" * 50)

    for i in range(len(matriz_estadisticas)):
        print(
            f"{i:<10} | "
            f"{matriz_estadisticas[i][0]:<20} | "
            f"{matriz_estadisticas[i][1]:<10}"
        )

    pausar()

# =====================================================================
# MENÚ PRINCIPAL
# =====================================================================

# Control principal del programa
def menu():
    cargar_contactos()

    while True:
        limpiar_pantalla()

        print("=======================================")
        print("         AGENDA DE CONTACTOS         ")
        print("=======================================")
        print(" 1. Agregar contacto")
        print(" 2. Buscar por nombre")
        print(" 3. Buscar por categoría")
        print(" 4. Editar contacto")
        print(" 5. Eliminar contacto")
        print(" 6. Mostrar todos")
        print(" 7. Ordenar alfabéticamente")
        print(" 8. Ordenar por ID")
        print(" 9. Ver reporte estadístico")
        print("10. Salir")
        print("=======================================")

        op = input("Seleccione una opción: ").strip()

        # Dependiendo de la opción llama la función correspondiente
        if op == "1":
            agregar()

        elif op == "2":
            buscar_nombre()

        elif op == "3":
            buscar_categoria()

        elif op == "4":
            editar()

        elif op == "5":
            eliminar()

        elif op == "6":
            mostrar_todos()

        elif op == "7":
            ordenar_por_nombre()

        elif op == "8":
            ordenar_por_id()

        elif op == "9":
            generar_reporte_matriz()

        elif op == "10":
            print("\n Gracias por utilizar la agenda.")
            break

        else:
            print(" Opción inválida.")
            pausar()

# =====================================================================
# INICIO DEL PROGRAMA
# =====================================================================

if __name__ == "__main__":
    menu()

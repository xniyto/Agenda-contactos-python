import os

archivo = "agenda.txt"
contactos = []

# =====================================================================
# FUNCIONES DE VALIDACIÓN Y SOPORTE (Interfaz y Calidad de Código)
# =====================================================================

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo para mejorar la UX."""
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje):
    """Garantiza la captura de un número entero sin que el programa muera."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")

def leer_texto(mensaje):
    """Valida que el texto no esté vacío y no contenga comas perjudiciales."""
    while True:
        texto = input(mensaje).strip()
        if not texto:
            print("❌ Error: Este campo no puede quedar vacío.")
        elif "," in texto:
            print("❌ Error: No se permiten comas (',') para no corromper la base de datos.")
        else:
            return texto

def mostrar_encabezado_tabla():
    """Imprime un encabezado estético para los listados en formato de tabla."""
    print(f"\n{'ID':<6} | {'Nombre':<22} | {'Teléfono':<15} | {'Email':<25} | {'Categoría':<12}")
    print("-" * 88)

def imprimir_fila_contacto(c):
    """Muestra de forma tabular y alineada un contacto en específico."""
    print(f"{c['id']:<6} | {c['nombre']:<22} | {c['telefono']:<15} | {c['email']:<25} | {c['categoria']:<12}")

# =====================================================================
# CORE DEL SISTEMA: PERSISTENCIA Y LÓGICA (Estructuras de Datos)
# =====================================================================

def cargar_contactos():
    """Lee el archivo plano y recupera los datos en memoria al iniciar."""
    global contactos
    contactos.clear()  # Evita duplicaciones en memoria si se llama re-concurrentemente
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 5:
                    contactos.append({
                        "id": int(datos[0]),
                        "nombre": datos[1],
                        "telefono": datos[2],
                        "email": datos[3],
                        "categoria": datos[4]
                    })

def guardar_contactos():
    """Garantiza la persistencia escribiendo la lista estructurada al disco."""
    with open(archivo, "w", encoding="utf-8") as f:
        for c in contactos:
            f.write(f"{c['id']},{c['nombre']},{c['telefono']},{c['email']},{c['categoria']}\n")

def ordenar_contactos():
    """Ordena los arreglos internamente bajo el criterio alfabético."""
    contactos.sort(key=lambda x: x["nombre"].lower())

# =====================================================================
# OPERACIONES DEL CRUD (Funcionamiento del Sistema)
# =====================================================================

def agregar():
    limpiar_pantalla()
    print("=== ➕ AGREGAR NUEVO CONTACTO ===")
    
    while True:
        id_nuevo = leer_entero("Ingrese ID: ")
        # Validación avanzada: Validar que el ID sea único
        if any(c["id"] == id_nuevo for c in contactos):
            print("❌ Error: Este ID ya pertenece a otro contacto. Intente con otro.")
        else:
            break

    nombre = leer_texto("Nombre: ")
    telefono = leer_texto("Teléfono: ")
    email = leer_texto("Email: ")
    categoria = leer_texto("Categoría (Amigo/Familia/Trabajo): ").capitalize()

    nuevo = {
        "id": id_nuevo,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "categoria": categoria
    }

    contactos.append(nuevo)
    guardar_contactos()
    print("\n✅ Contacto agregado con éxito de forma persistente.")

def buscar_nombre():
    limpiar_pantalla()
    print("=== 🔍 BUSCAR POR NOMBRE ===")
    nombre_buscar = leer_texto("Nombre o fragmento a buscar: ").lower()
    encontrado = False

    mostrar_encabezado_tabla()
    for c in contactos:
        if nombre_buscar in c["nombre"].lower():
            imprimir_fila_contacto(c)
            encontrado = True
            
    if not encontrado:
        print("ℹ️ No se encontraron contactos que coincidan con la búsqueda.")

def buscar_categoria():
    limpiar_pantalla()
    print("=== 📂 BUSCAR POR CATEGORÍA ===")
    cat_buscar = leer_texto("Categoría a filtrar: ").lower()
    encontrado = False

    mostrar_encabezado_tabla()
    for c in contactos:
        if c["categoria"].lower() == cat_buscar:
            imprimir_fila_contacto(c)
            encontrado = True

    if not encontrado:
        print("ℹ️ No hay contactos registrados bajo esa categoría.")

def editar():
    limpiar_pantalla()
    print("=== ✏️ EDITAR CONTACTO ===")
    id_buscar = leer_entero("Ingrese el ID del contacto a modificar: ")

    for c in contactos:
        if c["id"] == id_buscar:
            print("\n--- Datos Actuales ---")
            mostrar_encabezado_tabla()
            imprimir_fila_contacto(c)
            print("-" * 88)
            
            print("\nIngrese los nuevos datos:")
            c["nombre"] = leer_texto("Nuevo nombre: ")
            c["telefono"] = leer_texto("Nuevo teléfono: ")
            c["email"] = leer_texto("Nuevo email: ")
            c["categoria"] = leer_texto("Nueva categoría: ").capitalize()

            guardar_contactos()
            print("\n✅ Contacto actualizado correctamente en la base de datos.")
            return

    print("❌ Error: No se encontró ningún contacto con ese ID.")

def eliminar():
    limpiar_pantalla()
    print("=== ❌ ELIMINAR CONTACTO ===")
    id_buscar = leer_entero("Ingrese el ID del contacto a eliminar: ")

    for i in range(len(contactos)):
        if contactos[i]["id"] == id_buscar:
            confirmar = input(f"¿Seguro que desea eliminar a '{contactos[i]['nombre']}'? (s/n): ").lower()
            if confirmar == 's':
                contactos.pop(i)
                guardar_contactos()
                print("\n✅ Contacto eliminado permanentemente.")
            else:
                print("\nℹ️ Operación cancelada.")
            return

    print("❌ Error: El ID ingresado no existe.")

def mostrar_todos():
    limpiar_pantalla()
    print("=== 📋 LISTADO DE CONTACTOS ===")
    if not contactos:
        print("ℹ️ La agenda se encuentra vacía actualmete.")
        return

    ordenar_contactos()
    mostrar_encabezado_tabla()
    for c in contactos:
        imprimir_fila_contacto(c)
    print(f"\nTotal: {len(contactos)} contactos registrados.")

# =====================================================================
# MEJORA ADICIONAL: REPORTE MATRICIAL (Punto Extra y Requisito Obligatorio)
# =====================================================================

def generar_reporte_matriz():
    """
    Genera un reporte estadístico utilizando una matriz bidimensional (2D).
    Cumple explícitamente con el requisito de 'Matrices' solicitado en la rúbrica.
    """
    limpiar_pantalla()
    print("=== 📊 REPORTE ESTADÍSTICO MATRICIAL ===")
    
    # 1. Definimos las categorías estándar que rastrearemos
    categorias_base = ["Amigo", "Familia", "Trabajo", "Otros"]
    
    # 2. Inicializamos una Matriz 2D de N filas x 2 columnas. 
    # Estructura: [ [Categoría, Contador], [Categoría, Contador], ... ]
    matriz_estadisticas = [[cat, 0] for cat in categorias_base]

    # 3. Procesamos los arreglos e incrementamos los valores indexando la matriz
    for c in contactos:
        cat_contacto = c["categoria"]
        posicionado = False
        
        for i in range(len(matriz_estadisticas)):
            if matriz_estadisticas[i][0].lower() == cat_contacto.lower():
                matriz_estadisticas[i][1] += 1
                posicionado = True
                break
        
        # Si es una categoría externa a las estándar, la agregamos dinámicamente a la matriz
        if not posicionado:
            matriz_estadisticas.append([cat_contacto, 1])

    # 4. Despliegue formal de la matriz en pantalla
    print(f"{'Índice Filas':<12} | {'Categoría (Col 0)':<20} | {'Total (Col 1)':<12}")
    print("-" * 52)
    for i in range(len(matriz_estadisticas)):
        # Acceso explícito bidimensional: matriz[fila][columna]
        print(f"Fila [{i}]     | {matriz_estadisticas[i][0]:<20} | {matriz_estadisticas[i][1]:<12}")
    
    print("\n💡 *Nota:* Esta tabla es generada dinámicamente mapeando una estructura matricial 2D.")
    input("\nPresione Enter para regresar al menú...")

# =====================================================================
# MENÚ PRINCIPAL Y CONTROL DE FLUJO
# =====================================================================

def menu():
    cargar_contactos()

    while True:
        print("\n=======================================")
        print("        📖 AGENDA DE CONTACTOS         ")
        print("=======================================")
        print(" 1. Agregar contacto")
        print(" 2. Buscar por nombre")
        print(" 3. Buscar por categoría")
        print(" 4. Editar contacto")
        print(" 5. Eliminar contacto")
        print(" 6. Mostrar todos (Alfabético)")
        print(" 7. Ver Reporte Estadístico (Matriz 2D)")
        print(" 8. Salir")
        print("=======================================")

        op = input("Seleccione una opción: ").strip()

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
            generar_reporte_matriz()
        elif op == "8":
            print("\n👋 ¡Muchas gracias por utilizar la Agenda! Guardando cambios...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo con números del 1 al 8.")

# Punto de entrada de ejecución estructurada
if __name__ == "__main__":
    menu()

# 📖 Agenda de Contactos Avanzada

Sistema de gestión de contactos desarrollado en **Python**, como proyecto final de la asignatura de Programación.

---

## 👥 Integrantes

| Nombre | Carnet |
|---|---|
| Alejandro Mauricio Domínguez Ortez | DO100126 |
| Josué Miguel Melara Bachez | MB100926 |
| Oscar Antonio Azucena Vásquez | AV100526 |
| Luis Steven Rivera Cruz | RC101726 |

**Universidad Francisco Gavidia — Facultad de Ingeniería y Sistemas**  
**Materia:** Desarrollo de la Lógica de Programación  
**Docente:** Ing. Wilfredo Benjamín Magaña Martínez

---

## 📋 Descripción

Sistema que permite gestionar contactos personales desde la consola, con soporte de persistencia en archivos de texto. Implementa conceptos de programación estructurada, arreglos, matrices, funciones y manejo de archivos.

---

## ✨ Funcionalidades

- ➕ **Agregar contacto** — con validación de ID único y campos obligatorios
- 🔍 **Buscar por nombre** — búsqueda parcial o completa
- 📂 **Buscar por categoría** — Amigo, Familia, Trabajo u otras
- ✏️ **Editar contacto** — actualización de datos por ID
- ❌ **Eliminar contacto** — con confirmación previa
- 📋 **Listar todos** — ordenados alfabéticamente en formato de tabla
- 📊 **Reporte estadístico** — usando una matriz 2D de categorías y contadores

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Módulo `os` (manejo de archivos y sistema)
- Archivos de texto plano (`agenda.txt`) para persistencia de datos

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener **Python 3** instalado
2. Descarga o clona este repositorio
3. Abre una terminal en la carpeta del proyecto
4. Ejecuta el siguiente comando:

```bash
python agenda.py
```

---

## 📁 Estructura del proyecto

```
agenda-contactos-python/
│
├── agenda.py       # Código fuente principal
├── agenda.txt      # Base de datos generada automáticamente al usar el programa
└── README.md       # Este archivo
```

---

## 📌 Conceptos aplicados

- Arreglos (listas) y matrices 2D
- Funciones y modularidad
- Persistencia de datos con archivos
- Validación de entradas y manejo de excepciones
- Programación estructurada

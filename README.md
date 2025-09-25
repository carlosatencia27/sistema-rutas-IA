# Sistema Inteligente de Rutas (Proyecto IA)

Este proyecto implementa un **sistema inteligente basado en conocimiento** que determina la **mejor ruta** entre dos estaciones del sistema de transporte masivo local, utilizando **reglas lógicas** y el algoritmo de **búsqueda A\***.

---

## 👤 Integrante del Equipo

| Nombre completo       | Correo electrónico      | Rol en el proyecto (breve)                                                                 | Usuario Git/GitHub |
|----------------------|-----------------------|-------------------------------------------------------------------------------------------|------------------|
| Carlos Daniel Atencia | cdag2006@gmail.com | Responsable único: implementación del código, pruebas, documentación, registro de commits y presentación en video. | carlosatencia27 |

---

## 📖 Descripción

- **Base de Conocimiento:** Definida en `kb.txt` con hechos lógicos (`station(...)`, `edge(...)`, `coord(...)`, `transfer(...)`).
- **Algoritmo de Búsqueda:** Implementación de **A\*** para encontrar la mejor ruta según costo o duración.
- **Objetivo:** Facilitar la toma de decisiones para elegir rutas óptimas considerando transbordos, costo y tiempo.

---

## 🛠 Requisitos

- Python **3.8+**  
(No se requieren librerías externas, solo la biblioteca estándar de Python).

---

## ▶️ Ejecución

```bash
# Sintaxis
python route_finder.py kb.txt <origen> <destino> --optimize cost|duration|mixed

# Ejemplo
python route_finder.py kb.txt a f --optimize cost


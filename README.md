# Simulador de Gastos Personales

Este proyecto es una aplicacion en Pyhton que permite registrar, visualizar y calcular el total de los gastos personales de una persona. Se ha realizado con el fin de aplicar nuestros conocimientos en programación.

# Funcionalidades

## Funcionalidades Actuales

| #  | Descripción                                                                 |
|----|-----------------------------------------------------------------------------|
| 1  | **Registrar Gastos**: Permite registrar el monto, categoría, descripción y fecha del gasto. |
| 2  | **Listar Gastos**: Muestra los gastos de todos, por categoría o por rango de fechas. |
| 3  | **Calcular Gastos**: Calcula el total de los gastos de forma diaria, semanal (últimos 7 días) o mensual. |
| 4  | **Generar Reportes**: Crea reportes de los gastos diarios, semanales (últimos 7 días) y mensuales. |

## Funcionalidades a Futuro (En Construcción)

| #  | Descripción                                                                 |
|----|-----------------------------------------------------------------------------|
| 1  | **Guardar Reportes en archivo .json**: Permite almacenar los reportes generados en archivos JSON. |
| 2  | **Uso de Logins para Usuarios**: Implementar autenticación para gestionar los gastos de diferentes usuarios. |
| 3  | **Usar Tabulate**: Integrar la librería `tabulate` para mostrar las listas de gastos de forma ordenada y en formato tabla. |

---

### Recomendaciones para Mejoras:

- **Validaciones al Registrar Gastos**: Asegurarse de que el monto sea un número positivo y que la fecha esté en el formato correcto.
- **Mejoras en la Lista de Gastos**: Permitir ordenar los gastos por monto o fecha para facilitar la búsqueda.
- **Cálculos Acumulados**: Implementar un sistema de acumulado para los cálculos diarios, semanales y mensuales, y definir correctamente las fechas.
- **Exportación de Reportes**: Permitir la exportación de los reportes generados a formatos como CSV o PDF.

### Sugerencias para Futuro:

- **Persistencia de Datos**: Integrar una base de datos para mejorar el rendimiento a medida que el sistema escala.
- **Optimización de Cálculos**: Asegurarse de que los cálculos sean eficientes, especialmente al manejar grandes volúmenes de datos.
- **Interfaz de Usuario**: Crear una interfaz de usuario limpia e intuitiva, idealmente con un framework moderno como React o Vue.js.

---

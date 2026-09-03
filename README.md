# AgroCBA - Sistema de Gestión de Productos Agropecuarios

## Propósito

AgroCBA es una aplicación de consola desarrollada en Python que permite registrar y gestionar productos de una unidad productiva agropecuaria. Fue construida como prototipo monolítico donde la interfaz, las reglas de negocio y el manejo de datos conviven en un mismo programa.

## Institución

**SENA - Centro de Biotecnología Agropecuaria (CBA)**  
Programa: Tecnólogo en Análisis y Desarrollo de Software  
Ficha: 3409610

## Funcionalidades

- **Registrar producto:** agrega un nuevo producto con código, nombre, categoría, cantidad y precio. No permite códigos duplicados.
- **Consultar productos:** muestra en tabla todos los productos registrados.
- **Buscar producto:** encuentra un producto por su código y muestra todos sus datos.
- **Actualizar producto:** modifica los datos de un producto existente conservando su código.
- **Eliminar producto:** elimina un producto por código, solicitando confirmación antes de ejecutar.
- **Valor del inventario:** calcula y muestra la suma de cantidad × precio para todos los productos.

## Tecnologías

- Python 3
- Git (control de versiones)

## Instrucciones de ejecución

1. Clona o descarga el repositorio.
2. Abre una terminal y navega hasta la carpeta del proyecto:
   ```bash
   cd agrocba
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```
4. Selecciona una opción del menú y sigue las instrucciones en pantalla.

## Estructura del proyecto

```
agrocba/
├── main.py       # Código fuente principal de la aplicación
├── README.md     # Documentación del proyecto
└── .gitignore    # Archivos excluidos del control de versiones
```

## Autor

Aprendiz: Ismael Palencia Bolivar 
Ficha: 3409610

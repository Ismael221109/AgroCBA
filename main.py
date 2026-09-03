import json
import os

ARCHIVO_DB = "inventario_agrocba.json"

productos = []

def cargar_datos():
    """Carga los productos desde el archivo JSON al iniciar el programa."""
    global productos
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, "r", encoding="utf-8") as archivo:
                productos = json.load(archivo)
        except Exception as e:
            print(f" Error al cargar la base de datos: {e}")
            productos = []
    else:
        productos = []

def guardar_datos():
    """Guarda la lista actual de productos en el archivo JSON."""
    try:
        with open(ARCHIVO_DB, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f" Error al guardar los datos en el archivo: {e}")






def mostrar_menu():
    print("\n" + "=" * 45)
    print("SISTEMA AGROCBA")
    print("=" * 45)
    print(" 1. Registrar producto")
    print(" 2. Consultar productos")
    print(" 3. Buscar producto")
    print(" 4. Actualizar producto")
    print(" 5. Eliminar producto")
    print(" 6. Mostrar valor total del inventario")
    print(" 7. Mostrar la cantidad total de unidades existentes")
    print(" 8. Producto de mayor precio")
    print(" 9. Producto con mayor cantidad disponible")
    print(" 10. Consultar productos por categoría")
    print(" 11. Ordenar productos alfabéticamente")
    print(" 12. Mostrar productos con bajo inventario")
    print(" 13. Salir")
    print("=" * 45)

def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")
    while True:
        codigo = input("Código (ej. P001): ").strip()
        if not codigo:
            print(" El código no puede quedar vacío.")
        elif buscar_por_codigo(codigo):
            print(f" El código '{codigo}' ya existe. Use uno diferente.")
        else:
            break
            
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print(" El nombre no puede quedar vacío.")
        else:
            break
            
    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print(" La categoría no puede quedar vacía.")
        else:
            break
            
    cantidad = validar_entero_no_negativo("Cantidad (entero ≥ 0): ")
    precio = validar_numero_positivo("Precio (mayor que 0): ")
    
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    productos.append(producto)
    guardar_datos()
    print(f" Producto '{nombre}' registrado correctamente.")

def consultar_productos():
    print("\n--- CONSULTAR PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados.")
        return
    print(f"\n{'Código':<8} {'Nombre':<25} {'Categoría':<15} {'Cantidad':>9} {'Precio':>12}")
    print("-" * 72)
    for p in productos:
        print(
            f"{p['codigo']:<8} {p['nombre']:<25} {p['categoria']:<15} "
            f"{p['cantidad']:>9} {p['precio']:>12,.2f}"
        )
    print(f"\nTotal de productos: {len(productos)}")

def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código a buscar: ").strip()
    producto = buscar_por_codigo(codigo)
    if not producto:
        print(f" Producto con código '{codigo}' no encontrado.")
        return
    print("\n Datos del producto:")
    print(f" Código    : {producto['codigo']}")
    print(f" Nombre    : {producto['nombre']}")
    print(f" Categoría : {producto['categoria']}")
    print(f" Cantidad  : {producto['cantidad']}")
    print(f" Precio    : {producto['precio']:,.2f}")

def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    producto = buscar_por_codigo(codigo)
    if not producto:
        print(f" Producto con código '{codigo}' no encontrado.")
        return
        
    print(f"\nProducto actual: {producto['nombre']} | {producto['categoria']} | "
          f"Cant: {producto['cantidad']} | Precio: {producto['precio']:,.2f}")
    print("(Deje vacío para conservar el valor actual)\n")
    
    nuevo_nombre = input(f"Nuevo nombre [{producto['nombre']}]: ").strip()
    if nuevo_nombre:
        producto["nombre"] = nuevo_nombre
        
    nueva_cat = input(f"Nueva categoría [{producto['categoria']}]: ").strip()
    if nueva_cat:
        producto["categoria"] = nueva_cat
        
    entrada_cant = input(f"Nueva cantidad [{producto['cantidad']}]: ").strip()
    if entrada_cant:
        producto["cantidad"] = validar_entero_no_negativo(
            f"Nueva cantidad [{producto['cantidad']}]: ", valor_previo=entrada_cant
        )
        
    entrada_precio = input(f"Nuevo precio [{producto['precio']}]: ").strip()
    if entrada_precio:
        producto["precio"] = validar_numero_positivo(
            f"Nuevo precio [{producto['precio']}]: ", valor_previo=entrada_precio
        )
    guardar_datos()
    print(f" Producto '{producto['codigo']}' actualizado correctamente.")

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    producto = buscar_por_codigo(codigo)
    if not producto:
        print(f" Producto con código '{codigo}' no encontrado.")
        return
    print(f"\nSe eliminará: {producto['nombre']} ({producto['codigo']})")
    confirmacion = input("¿Confirma la eliminación? (s/n): ").strip().lower()
    if confirmacion == "s":
        productos.remove(producto)
        guardar_datos()
        print(f" Producto '{codigo}' eliminado.")
    else:
        print("Eliminación cancelada. El producto permanece registrado.")

def calcular_inventario():
    print("\n--- VALOR TOTAL DEL INVENTARIO ---")
    if not productos:
        print("No hay productos registrados.")
        return
    total = sum(p["cantidad"] * p["precio"] for p in productos)
    print(f"\n{'Código':<8} {'Nombre':<25} {'Cant':>6} {'Precio':>12} {'Subtotal':>14}")
    print("-" * 68)
    for p in productos:
        subtotal = p["cantidad"] * p["precio"]
        print(f"{p['codigo']:<8} {p['nombre']:<25} {p['cantidad']:>6} "
              f"{p['precio']:>12,.2f} {subtotal:>14,.2f}")
    print("-" * 68)
    print(f"{'VALOR TOTAL DEL INVENTARIO':>52}: {total:>14,.2f}")

def buscar_por_codigo(codigo):
    for p in productos:
        if p["codigo"].upper() == codigo.upper():
            return p
    return None

def validar_entero_no_negativo(mensaje, valor_previo=None):
    entrada = valor_previo
    while True:
        if entrada is None:
            entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print(" La cantidad debe ser un número entero mayor o igual a cero.")
                entrada = None
            else:
                return valor
        except ValueError:
            print(" Ingrese un número entero válido.")
            entrada = None

def validar_numero_positivo(mensaje, valor_previo=None):
    entrada = valor_previo
    while True:
        if entrada is None:
            entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print(" El precio debe ser mayor que cero.")
                entrada = None
            else:
                return valor
        except ValueError:
            print(" Ingrese un número válido.")
            entrada = None

def total_cantidad_producto():
    print("\n--- CANTIDAD TOTAL DE UNIDADES ---")
    if not productos:
        print("No hay productos registrados.")
        return
    total_unidades = sum(p["cantidad"] for p in productos)
    print(f"La cantidad total de unidades existentes en bodega es: {total_unidades}")

def producto_mayor_precio():
    print("\n--- PRODUCTO DE MAYOR PRECIO ---")
    if not productos:
        print("No hay productos registrados.")
        return
    p_max = max(productos, key=lambda x: x["precio"])
    print(f"Producto más costoso: {p_max['nombre']} ({p_max['codigo']})")
    print(f"Precio: {p_max['precio']:,.2f} | Stock: {p_max['cantidad']} uds.")

def producto_mayor_disponible():
    print("\n--- PRODUCTO CON MAYOR CANTIDAD DISPONIBLE ---")
    if not productos:
        print("No hay productos registrados.")
        return
    p_max_cant = max(productos, key=lambda x: x["cantidad"])
    print(f"Producto con mayor stock: {p_max_cant['nombre']} ({p_max_cant['codigo']})")
    print(f"Cantidad disponible: {p_max_cant['cantidad']} uds. | Precio: {p_max_cant['precio']:,.2f}")

def consultar_categoria():
    print("\n--- CONSULTAR PRODUCTOS POR CATEGORÍA ---")
    if not productos:
        print("No hay productos registrados.")
        return
    categoria_buscar = input("Ingrese la categoría a consultar: ").strip().lower()
    filtrados = [p for p in productos if p["categoria"].lower() == categoria_buscar]
    
    if not filtrados:
        print(f"No se encontraron productos en la categoría '{categoria_buscar}'.")
        return
        
    print(f"\n{'Código':<8} {'Nombre':<25} {'Cantidad':>9} {'Precio':>12}")
    print("-" * 56)
    for p in filtrados:
        print(f"{p['codigo']:<8} {p['nombre']:<25} {p['cantidad']:>9} {p['precio']:>12,.2f}")

def orden_alfabetico():
    print("\n--- PRODUCTOS ORDENADOS ALFABÉTICAMENTE ---")
    if not productos:
        print("No hay productos registrados.")
        return
    productos_ordenados = sorted(productos, key=lambda x: x["nombre"].lower())
    
    print(f"\n{'Nombre':<25} {'Código':<8} {'Categoría':<15} {'Cantidad':>9}")
    print("-" * 60)
    for p in productos_ordenados:
        print(f"{p['nombre']:<25} {p['codigo']:<8} {p['categoria']:<15} {p['cantidad']:>9}")

def productos_bajo_inventario():
    print("\n--- PRODUCTOS CON BAJO INVENTARIO ---")
    if not productos:
        print("No hay productos registrados.")
        return
        
    LIMITE_ALERTA = 5
    bajo_stock = [p for p in productos if p["cantidad"] <= LIMITE_ALERTA]
    
    if not bajo_stock:
        print(f"¡Excelente! No hay productos con stock menor o igual a {LIMITE_ALERTA} unidades.")
        return
        
    print(f"\n¡ALERTA! Productos con stock menor o igual a {LIMITE_ALERTA} unidades:")
    print(f"\n{'Código':<8} {'Nombre':<25} {'Cantidad':>9}")
    print("-" * 45)
    for p in bajo_stock:
        print(f"{p['codigo']:<8} {p['nombre']:<25} {p['cantidad']:>9}")

def main():
    cargar_datos()
    
    opciones = {
        "1": registrar_producto,
        "2": consultar_productos,
        "3": buscar_producto,
        "4": actualizar_producto,
        "5": eliminar_producto,
        "6": calcular_inventario,
        "7": total_cantidad_producto,
        "8": producto_mayor_precio,
        "9": producto_mayor_disponible,
        "10": consultar_categoria,
        "11": orden_alfabetico,
        "12": productos_bajo_inventario
    }
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion in opciones:
            opciones[opcion]() 
        elif opcion == "13":
            print("\nGracias por usar el Sistema AgroCBA. ¡Hasta pronto!\n")
            break
        else:
            print(f" Opción '{opcion}' inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

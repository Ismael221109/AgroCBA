
productos = []



def mostrar_menu():
    print("\n" + "=" * 45)
    print("           SISTEMA AGROCBA")
    print("=" * 45)
    print("  1. Registrar producto")
    print("  2. Consultar productos")
    print("  3. Buscar producto")
    print("  4. Actualizar producto")
    print("  5. Eliminar producto")
    print("  6. Mostrar valor total del inventario")
    print("  7. Salir")
    print("=" * 45)



def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")

    while True:
        codigo = input("Código (ej. P001): ").strip()
        if not codigo:
            print(" El código no puede quedar vacío.")
        elif buscar_por_codigo(codigo):
            print(f"  El código '{codigo}' ya existe. Use uno diferente.")
        else:
            break


    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("  El nombre no puede quedar vacío.")
        else:
            break


    while True:
        categoria = input("Categoría: ").strip()
        if not categoria:
            print("  La categoría no puede quedar vacía.")
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
        print(f"  Producto con código '{codigo}' no encontrado.")
        return

    print("\n  Datos del producto:")
    print(f"  Código    : {producto['codigo']}")
    print(f"  Nombre    : {producto['nombre']}")
    print(f"  Categoría : {producto['categoria']}")
    print(f"  Cantidad  : {producto['cantidad']}")
    print(f"  Precio    : {producto['precio']:,.2f}")



def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    producto = buscar_por_codigo(codigo)

    if not producto:
        print(f"  Producto con código '{codigo}' no encontrado.")
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

    print(f"  Producto '{producto['codigo']}' actualizado correctamente.")



def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    producto = buscar_por_codigo(codigo)

    if not producto:
        print(f"  Producto con código '{codigo}' no encontrado.")
        return

    print(f"\nSe eliminará: {producto['nombre']} ({producto['codigo']})")
    confirmacion = input("¿Confirma la eliminación? (s/n): ").strip().lower()

    if confirmacion == "s":
        productos.remove(producto)
        print(f"  Producto '{codigo}' eliminado.")
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
    """Retorna el diccionario del producto si existe, o None."""
    for p in productos:
        if p["codigo"].upper() == codigo.upper():
            return p
    return None


def validar_entero_no_negativo(mensaje, valor_previo=None):
    """Pide un entero >= 0. Si valor_previo ya fue leído, lo valida directamente."""
    entrada = valor_previo
    while True:
        if entrada is None:
            entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print("  La cantidad debe ser un número entero mayor o igual a cero.")
                entrada = None
            else:
                return valor
        except ValueError:
            print("  Ingrese un número entero válido.")
            entrada = None


def validar_numero_positivo(mensaje, valor_previo=None):
    """Pide un número > 0. Si valor_previo ya fue leído, lo valida directamente."""
    entrada = valor_previo
    while True:
        if entrada is None:
            entrada = input(mensaje).strip()
        try:
            valor = float(entrada)
            if valor <= 0:
                print("  El precio debe ser mayor que cero.")
                entrada = None
            else:
                return valor
        except ValueError:
            print("  Ingrese un número válido.")
            entrada = None



def main():
    opciones = {
        "1": registrar_producto,
        "2": consultar_productos,
        "3": buscar_producto,
        "4": actualizar_producto,
        "5": eliminar_producto,
        "6": calcular_inventario,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion in opciones:
            opciones[opcion]()
        elif opcion == "7":
            print("\nGracias por usar el Sistema AgroCBA. ¡Hasta pronto!\n")
            break
        else:
            print(f"  Opción '{opcion}' inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

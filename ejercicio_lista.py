productos = []
total_pedido = 0

producto = input("Ingrese producto " "(o 'fin'): ").strip().lower()

while producto != "fin":
    try:
        precio = float(input("Precio: $"))
        cantidad = int(input("Cantidad: "))
        productos.append(producto)
        total_pedido += precio * cantidad
    except ValueError:
        print("Dato inválido, no se agrega.")
    producto = input("Ingrese producto " "(o 'fin'): ").strip().lower()

print("Detalle del pedido:")
for p in productos:
    print("-", p)
print("Total: $", total_pedido)
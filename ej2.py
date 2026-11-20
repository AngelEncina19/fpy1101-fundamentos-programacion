def calcular_total(producto, cantidad, precios):
    if producto in precios:
        return precios[producto] * cantidad
    else:
        return 0

precios = {"cafe": 1000, "queque": 1500, "jugo": 1200}
total_pedido = 0

producto = input("Ingrese producto (o 'fin' para terminar): ").strip().lower()

while producto != "fin":
    try:
        cantidad = int(input("Ingrese cantidad: "))
        total_pedido = total_pedido + calcular_total(producto, cantidad, precios)
    except ValueError:
        print("Cantidad inválida, producto no agregado.")
    producto = input("Ingrese producto (o 'fin' para terminar): ").strip().lower()

print("Total del pedido: $", total_pedido)
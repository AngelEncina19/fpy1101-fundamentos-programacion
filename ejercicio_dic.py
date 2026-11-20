precios = {"cafe": 1000, "queque": 1500, "jugo": 1200, "sandwich": 1500}

print("Precio del café:", precios["cafe"])
print("Precio del quque:", precios["queque"])
print("Precio del sandwich:", precios["sandwich"])

precios["te"] = 900    # Agrega clave nueva
precios["cafe"] = 1100 # Actualiza clave existente

print(precios)

# Función con parámetros y return
def calcular_total(precio, cantidad):
    return precio * cantidad

# Ejemplo de uso puntual (como en la guía)
total_cafe = calcular_total(precios["cafe"], 2)
print("Total café (x2):", total_cafe)

# Recorrer el diccionario y calcular el total de cada producto (ej. 2 unidades de cada uno)
cantidad_por_producto = 2
for producto, precio in precios.items():
    total = calcular_total(precio, cantidad_por_producto)
    print(f"{producto} (x{cantidad_por_producto}) cuesta $ {total}")
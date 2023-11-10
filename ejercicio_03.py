precios = {'pan': 1.40,'huevos': 2.30,'cebolla': 0.85,'aceite': 4.35}
articulo = input("Escribe el artículo a comprar: ")
if articulo in precios:
    cantidad = int(input("Escribe la cantidad: "))
    total = precios[articulo] * cantidad
    print("El precio total es:", total)
else:
    print("El artículo no está en la lista de precios.")
input()
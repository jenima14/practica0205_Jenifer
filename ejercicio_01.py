diccionary = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
usuario = input("Escribir el nombre de la divisa: ")
if usuario in diccionary:
    simbolo = diccionary[usuario]
    print("El símbolo de", usuario, "es:", simbolo)
else:
    print("La divisa no está en el diccionario, escribir una divisa válida.")
    input()
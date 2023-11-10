B_datos = {}
while True:
    print("\nMenú Principal:")
    print(" 1) Añadir alumno(a)")
    print(" 2) Eliminar alumno(a)")
    print(" 3) Mostrar alumno(a)")
    print(" 4) Lista de todo el alumnado")
    print(" 5) Lista del alumnado aprobado")
    print(" 6) Terminar")
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == '1':
        nif = input("Escribe el NIF del alumno(a): ")
        nombre = input("Escribe el nombre del alumno(a): ")
        aprobado = input("Aprobado(a) (si/no): ").lower() == 'si'
        B_datos[nif] = {'Nombre': nombre, 'Aprobado': aprobado}
        print("Alumno(a) añadido(a) correctamente.")
    
    elif opcion == '2':
        nif = input("Escribe el NIF del alumno(a) a eliminar: ")
        if nif in B_datos:
            del B_datos[nif]
            print("Alumno(a) eliminado(a) correctamente.")
        else:
            print("El NIF no se encuentra en la base de datos.")

    elif opcion == '3':
        nif = input("Escribe el NIF del alumno(a) a mostrar: ")
        if nif in B_datos:
            print(f"\nDatos del alumno(a) con NIF {nif}:")
            print(f"Nombre: {B_datos[nif]['Nombre']}")
            print(f"Aprobado: {B_datos[nif]['Aprobado']}")
        else:
            print("El NIF no se encuentra en la base de datos.")

    elif opcion == '4':
        print("\nLista de todo el alumnado:")
        for nif, datos_alumno in B_datos.items():
            print(f"NIF: {nif}, Nombre: {datos_alumno['Nombre']}")

    elif opcion == '5':
        print("\nListado de alumnado aprobado:")
        for nif, datos_alumno in B_datos.items():
            if datos_alumno['Aprobado']:
                print(f"NIF: {nif}, Nombre: {datos_alumno['Nombre']}")

    elif opcion == '6':
        print("Programa terminado.")
        break

    else:
        print("Opción no válida, selecciona una opción del 1 al 6.")
input()
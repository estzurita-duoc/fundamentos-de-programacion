inventario= [{"codigo": "",
               "titulo": "",
                 "autor": "",
                   "cantidad": 0,
                    "precio": 0.0}]
def registro():

    codigo_valido = False

    while codigo_valido == False:
        codigo_nuevo = input("ingrese el codigo del libro: ")

        for libro in inventario:
            if libro["codigo"] == codigo_nuevo:
                print("El codigo ya existe, por favor ingrese un codigo diferente.")
                break
        else:
            codigo_valido = True 

    titulo_libro = input("ingrese el titulo del libro: ")
    autor_libro = input("ingrese el autor del libro: ")

    while True:
        try:
            cantidad_libro = int(input("ingrese la cantidad de libros: "))
            break
        except ValueError:
            print("Por favor ingrese un numero entero para la cantidad.")
    while True:
        try:
            precio_libro = float(input("ingrese el precio del libro: "))
            break
        except ValueError:
            print("Por favor ingrese un numero valido para el precio.")
    
    nuevo_libro = {
        "codigo": codigo_nuevo,
        "titulo": titulo_libro,
        "autor": autor_libro,
        "cantidad": cantidad_libro,
        "precio": precio_libro
    }

    inventario.append(nuevo_libro)
    print("Libro registrado exitosamente.")

def buscar_libro():
    codigo_buscar= input("ingrese el codigo del libro a buscar: ")
    for libro in inventario:
        if libro["codigo"] == codigo_buscar:
            

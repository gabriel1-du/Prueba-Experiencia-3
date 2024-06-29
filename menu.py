from funciones import menu,suma_lista
import random


#listas y diccionarios para almacenar datos
producto = {}
categoria = []
lista_productos = []
precios = []
#con esta fnuncion se mostrara las opciones al usuario
 
while True : 
    try : 
        menu()

        #Esta variable guarda la opcion del usuario 
        opcion_usuario = int(input("Ingrese una opcion : "))

        if opcion_usuario == 1 :
            #Se le pide al usuario que se ingrese los datos del producto
            nombre = input("Ingrese el nombre del producto :")
            categoria = input("Ingrese la categoria del producto : ")
            cantidad =  input("Ingrese la cantidad : ")
            precio = random.randint(1,1000) 
            precios.append(precio)

            
            
            #Se usa un diccionario para guardar la informacion del producto
            producto["Producto"] = {"Nombre": nombre, "categoria": categoria, "cantidad " : cantidad, "precio" : precio }
        
                                            
        elif opcion_usuario == 2 :
            print(lista_productos)

        elif opcion_usuario == 4 : 
            #una variable para la cantidad de productos y la otra para suma, asi se genera la operacion de promedio
            suma_precios = sum(precios)
            cantidad_precios = len(precios)
            print(cantidad_precios)
        
        else : 
            print("Usted a salido del programa : ")
            #se transcribe la lista al archuvo txt
            with open("texto.txt","add") as archivo :
                archivo.write(lista_productos) 
            break
    except ValueError : 
        print("Ingrese datos que correspondan ")
    finally :
        print("El programa no terminara hasta que ingrese algo correspendiente a lo pedido")
    


        





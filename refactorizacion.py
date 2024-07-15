def ingresar_puntuacion_comentario():
    while True:
        print ("introduzca una puntuacion en una escala de 1 a 5")
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print("introduzca una puntuacion en una escala de 1 a 5")
            else:
                print("Ingrese un comentario")
                comment = input()
                post = f"punto: {point}, comentario: {comment}"
                with open("data.txt", "a") as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print("introduzca un valor numerico")

def comprobar_resultados():
    print("Resultados hasta la fecha:")
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def finalizar_programa():
    print("Finalizando...")
    quit()

def seleccionar_proceso():
 while True:
    print("Seleccione el proceso que desea aplicar")
    print("1: Ingresar puntuación y comentario")
    print("2: Comprobar los resultados obtenidos")
    print("3: Finalizar")
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            ingresar_puntuacion_comentario()
        elif num == 2:
            comprobar_resultados()
        elif num == 3:
            finalizar_programa()
        else:
            print("Ingrese un número del 1 al 3")
    else:
        print("Ingrese un número del 1 al 3")
# Ejecucion del programa        
seleccionar_proceso()
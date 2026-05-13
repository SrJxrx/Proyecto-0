#Variables globales(en el main con global)
cifrado = ["Cifrado César", "Cifrado Monoalfabético", "Cifrado Vigenère", "Cifrado PlayFair modificado", "Cifrado Rail Fence", "Escítala"]
abecedario = ("abcdefghijklmnñopqrstuvwxyz")

#Cesar codificación y decodificación.

def cesarCod(codificar, movimiento):
    codificando = ""
    for letra in codificar:
        if letra != " ":
            índice = (abecedario.find(letra) + movimiento) % len(abecedario)
            codificando += abecedario[índice]
        else:
            codificando += letra
    print()
    print("El texto cifrado es:", codificando)

def cesarDec(decodificar, movimiento):
    decodificando = ""
    for letra in decodificar:
        if letra != " ":
            índice = (abecedario.find(letra) - movimiento) % len(abecedario)
            decodificando += abecedario[índice]
        else:
            decodificando += letra
    print()
    print("El texto descifrado es:", decodificando)

#Monoalfabetico codificación y decodificación.

def monoCod(texto,palabra):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_cifrado = ""
    texto_cifrado = ""
    for letra in palabra:
        if letra not in abecedario_cifrado:
            abecedario_cifrado+=letra
    for letra in abecedario:
        if letra not in abecedario_cifrado:
            abecedario_cifrado+=letra
                 
    for letra in texto:
        if letra == " ":
            texto_cifrado+= " "
        else:    
            posicion = abecedario.index(letra)
            letra_cifrada = abecedario_cifrado[posicion]
            texto_cifrado += letra_cifrada

    print("El mensaje cifrado es: " + texto_cifrado)



def monoDec(texto,palabra):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_cifrado = ""
    texto_descifrado = ""
    for letra in palabra:
        if letra not in abecedario_cifrado:
            abecedario_cifrado+=letra
    for letra in abecedario:
        if letra not in abecedario_cifrado:
            abecedario_cifrado+=letra
                     
    for letra in texto:
        if letra == " ":
            texto_descifrado+= " "
        else:
            posicion = abecedario_cifrado.index(letra)
            letra_descifrada = abecedario[posicion]
            texto_descifrado += letra_descifrada

    print("El mensaje descifrado es: " + texto_descifrado)
#Vigenere codificación y decodificación.

def vigenereCod(texto,palabra):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto = list(texto)
    palabra = list(palabra)
    cifrado = []
    posicion2 = 0
    for posicion in range (len(texto)):
        if texto[posicion] != " ":
            valor = texto[posicion]
            letra1 = abecedario.find(valor)
            if posicion2 != len(palabra):
                valor = palabra[posicion2]
                letra2 = abecedario.find(valor)
                posicion2 += 1
            else:
                posicion2 = 0
                valor = palabra[posicion2]
                letra2 = abecedario.find(valor)
                posicion2 +=1
            suma = letra1+letra2
            if suma < 26:
             cifrado.insert(posicion,abecedario[suma])
            else:
             suma = suma % 27
             cifrado.insert(posicion,abecedario[suma])   
        else:
            cifrado.insert(posicion," ")
    delimitador = " " 
    mensajeFinal = delimitador.join(cifrado)
    print("El mensaje cifrado es: ",mensajeFinal)

def vigenereDec(texto,palabra):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto = list(texto)
    palabra = list(palabra)
    cifrado = []
    posicion2 = 0
    for posicion in range (len(texto)):
        if texto[posicion] != " ":
            valor = texto[posicion]
            letra1 = abecedario.find(valor)
            if posicion2 != len(palabra):
                valor = palabra[posicion2]
                letra2 = abecedario.find(valor)
                posicion2 += 1
            else:
                posicion2 = 0
                valor = palabra[posicion2]
                letra2 = abecedario.find(valor)
                posicion2 +=1
            resta = letra1-letra2
            if resta > 0:
             cifrado.insert(posicion,abecedario[resta])
            else:
             resta = resta % 27
             cifrado.insert(posicion,abecedario[resta])   
        else:
            cifrado.insert(posicion," ")
    delimitador = " " 
    mensajeFinal = delimitador.join(cifrado)
    print("El mensaje descifrado es: ",mensajeFinal)

#Playfair codificación y decodificación.

def playfairCod(codificar, código):
    #Preparación de palabra clave
    abecedario = "abcdefghijklmnñopqrstuvwxyz123"
    for letra in abecedario:
        if letra in código:
            abecedario = abecedario.replace(letra, "")
    #Formación de matriz
    código += abecedario
    matriz = []
    for i in range(0, len(código), 5):
        matriz.append(list(código[i: i + 5]))
    #Primeras fases de codificación del texto
    codificando = ""
    verificar = ""
    for letra in codificar:
        if letra == verificar:
            codificando += "1"
        verificar = letra
        codificando += letra
    codificando = codificando.split(" ")
    for i in range(0, len(codificando)):
        if len(codificando[i]) % 2 != 0:
            codificando[i] += "1"
    #Separación de cada palabra del texto a codificar en dos letras (+ INFO TEMPORAL)
    codificación = []
    for i in range(0, len(codificando)):
        for j in range(0, len(codificando[i]), 2):
            codificación.append(codificando[i][j: j + 2])
    for i in range(0, len(codificación)):
        for j in range(0, 6):
            if codificación[i][0] in matriz[j]:
                letrafila1 = j
            if codificación[i][1] in matriz[j]:
                letrafila2 = j
        letracolumna1 = matriz[letrafila1].index(codificación[i][0])
        letracolumna2 = matriz[letrafila2].index(codificación[i][1])
        if letrafila1 == letrafila2:
            if letracolumna1 == 4:
                letracolumna1 = -1
            if letracolumna2 == 4:
                letracolumna2 = -1
            codificación[i] = matriz[letrafila1][letracolumna1 + 1] + matriz[letrafila2][letracolumna2 + 1]
        elif letracolumna1 == letracolumna2:
            if letrafila1 == 5:
                letrafila1 = -1
            if letrafila2 == 5:
                letrafila2 = -1
            codificación[i] = matriz[letrafila1 + 1][letracolumna1] + matriz[letrafila2 + 1][letracolumna2]
        else:
            codificación[i] = matriz[letrafila1][letracolumna2] + matriz[letrafila2][letracolumna1]
    codificar = ""
    for i in range(0, len(codificando)):
        for j in range(0, len(codificando[i]), 2):
            codificar += codificación.pop(0)
        codificar += " "
    print()
    print("El texto cifrado con PlayFair es:", codificar)

def playfairDec(decodificar, código):
    decodificar = decodificar.split(" ")
    for i in range(0, len(decodificar)):
        if len(decodificar[i]) % 2 != 0:
            raise Exception("Todas las palabras del texto a decodificar deben tener una cantidad de letras par.")
    #Preparación de palabra clave
    abecedario = "abcdefghijklmnñopqrstuvwxyz123"
    for letra in abecedario:
        if letra in código:
            abecedario = abecedario.replace(letra, "")
    #Formación de matriz
    código += abecedario
    matriz = []
    for i in range(0, len(código), 5):
        matriz.append(list(código[i: i + 5]))
    #Separación de cada palabra del texto a decodificar en dos letras
    decodificación = []
    for i in range(0, len(decodificar)):
        for j in range(0, len(decodificar[i]), 2):
            decodificación.append(decodificar[i][j: j + 2])
    for i in range(0, len(decodificación)):
        for j in range(0, 6):
            if decodificación[i][0] in matriz[j]:
                letrafila1 = j
            if decodificación[i][1] in matriz[j]:
                letrafila2 = j
        letracolumna1 = matriz[letrafila1].index(decodificación[i][0])
        letracolumna2 = matriz[letrafila2].index(decodificación[i][1])
        if letrafila1 == letrafila2:
            if letracolumna1 == 4:
                letracolumna1 = -1
            if letracolumna2 == 4:
                letracolumna2 = -1
            decodificación[i] = matriz[letrafila1][letracolumna1 - 1] + matriz[letrafila2][letracolumna2 - 1]
        elif letracolumna1 == letracolumna2:
            if letrafila1 == 5:
                letrafila1 = -1
            if letrafila2 == 5:
                letrafila2 = -1
            decodificación[i] = matriz[letrafila1 - 1][letracolumna1] + matriz[letrafila2 - 1][letracolumna2]
        else:
            decodificación[i] = matriz[letrafila1][letracolumna2] + matriz[letrafila2][letracolumna1]
    decodificando = ""
    for i in range(0, len(decodificar)):
        for j in range(0, len(decodificar[i]), 2):
            decodificando += decodificación.pop(0)
        decodificando += " "
    decodificando = decodificando.replace("1", "")
    print()
    print("El texto cifrado con PlayFair es:", decodificando)

#Railfence codificación y decodificación.

def railfenceCod(texto):

def railfenceDec(texto):

#Escitala codificación y decodificación.

def escitalaCod(texto, lineas):

def escitalaDec(texto, lineas):

def valorarRestriccionesPalabra(palabra, decisión):
    if decisión == "2":
        #Restricciones Palabra Cifrado Monoalfabético
    if decisión == "3":
        #Restricciones Palabra Cifrado Vigenère
    if decisión == "4":
        if any(letra not in abecedario for letra in palabra):
            raise Exception("La palabra clave no puede tener números, símbolos ni espacios.")

def valorarRestriccionesTexto(texto, decisión):
    if decisión == "1":
        if any(letra not in abecedario for letra in texto):
            raise Exception("El texto no puede tener símbolos ni números")
    if decisión == "2":
        #Restricciones Texto Cifrado Monoalfabético
    if decisión == "3":
        #Restricciones Texto Cifrado Vigenère
    if decisión == "4":
        if any(letra not in abecedario + "123 " for letra in texto):
            raise Exception("El texto no puede tener símbolos o números diferentes a 1, 2 y 3.")
    if decisión == "5":
        #Restricciones Texto Cifrado Rail Fence
    if decisión == "6":
        #Restricciones Texto Escítala

def prepararTexto(frase):
    while frase[-1] == " ":
        frase = frase[: -1]
    if type(frase) != str:
        raise Exception("El texto debe ser un string.")
    texto = ""
    for letra in frase.lower():
        if letra == " " and letra == texto[len(texto) - 1]:
            texto = texto[: -1]
        texto += letra
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto

def prepararPalabra(clave):
    if type(clave) != str:
        raise Exception("El texto debe ser un string.")
    código = ""
    for letra in clave.lower():
        if letra not in código:
            código += letra
    return código

def usarNuevamente(decisión):
    """Función que le pregunta al usuario si desea utilizar de nuevo el programa. Sólo acepta "S" o "N" como respuesta.
    Entradas y restricciones:
    - Ninguna.
    Salidas:
    Retorna True si el usuario escribe "S", False si no."""
    print()
    respuesta = input(f"¿Desea utilizar de nuevo el programa?\nÚltimo tipo de cifrado utilizado:\
 {cifrado[int(decisión) - 1]}.\nIngrese (S/N) como respuesta: ")
    respuesta = respuesta.lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta inválida. Inténtelo nuevamente.")
        respuesta = input("¿Desea utilizar de nuevo el programa? (S/N) ")
        respuesta = respuesta.lower()
    return respuesta == "s"

def main():
    """
    Programa principal del Proyecto-0.
    """
    try:
        global abecedario
        global cifrado
        print("¡Buen día usuario!")
        print("Bienvenido al sistema de codificación y decodificación.")
        print("Aqui podrá codificar un mensaje en el cifrado que desee.")
        print("Tambien puede decodificar un mensaje con el tipo de decifrado que desee.")
        continuar = True
        while continuar:
            print()
            print("Tipos de cifrados disponibles:")
            print("1. Cifrado César.")
            print("2. Cifrado Monoalfabético.")
            print("3. Cifrado Vigenère.")
            print("4. Cifrado PlayFair")
            print("5. Cifrado Rail Fence.")
            print("6. Escítala.")
            print("7. SALIR DEL PROGRAMA.")
            print()
            decisión = input("Su opción: ")
            while decisión not in ("1" , "2", "3", "4", "5", "6", "7"):
                print("Opción no válida")
                decisión = input("Su opción: ")
            if decisión != "7":
                print()
                print("¿Desea codificar o decodificar?")
                print("1. Codificar.")
                print("2. Decodificar.")
                print()
                opción = input("Su opción: ")
                while opción not in ("1", "2"):
                    print("Opción no válida")
                    opción = input("Su opción: ")
                if opción == "1":
                    mensaje = "codificar"
                    mensaje2 = "utilizará en la codificación"
                if opción == "2":
                    mensaje = "decodificar"
                    mensaje2 = "utilizó en la codificación"
                print()
                texto = input(f"Ingrese el texto que desea {mensaje}: ")
                texto = prepararTexto(texto)
                valorarRestriccionesTexto(texto, decisión)
                if decisión in ("2", "3", "4"):
                    print()
                    palabra = input(f"ingrese el palabra clave que se {mensaje2}: ")
                    palabra = prepararPalabra(palabra)
                    valorarRestriccionesPalabra(palabra, decisión)
                if decisión == "1":
                    try:
                        desplazamiento = int(input("Ingrese la cantidad de posiciones del desplazamiento: "))
                    except ValueError:
                        raise Exception("El valor del desplazamiento debe ser un número entero.")
                if opción == "1":
                    if decisión == "1":
                        #Subrutina Codificación Cifrado César
                        cesarCod(texto, desplazamiento)
                    if decisión == "2":
                       monoCod(texto,palabra)
                    if decisión == "3":
                        monoDec(texto,palabra)
                    if decisión == "4":
                        playfairCod(texto, palabra)
                    if decisión == "5":
                        #Subrutina Codificación Cifrado Rail Fence
                    if decisión == "6":
                        #Subrutina Codificación Escítala
                if opción == "2":
                    if decisión == "1":
                        #Subrutina Decodificación Cifrado César
                        cesarDec(texto, desplazamiento)
                    if decisión == "2":
                        #Subrutina Decodificación Cifrado Monoalfabético
                    if decisión == "3":
                        #Subrutina Decodificación Cifrado Vigenère
                    if decisión == "4":
                        playfairDec(texto, palabra)
                    if decisión == "5":
                        #Subrutina Decodificación Cifrado Rail Fence
                    if decisión == "6":
                        #Subrutina Decodificación Escítala
                continuar = usarNuevamente(decisión)
            else:
                continuar = False
        print()
        print("Gracias por utilizar este programa :)")
    except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
  main()


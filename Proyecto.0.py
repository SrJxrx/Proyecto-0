#Enviar usuario/perfil de GitHub a maviles@itcr.cr

#Variables globales(en el main con global)
cifrado = ["Cifrado César", "Cifrado Monoalfabético", "Cifrado Vigenère", "Cifrado PlayFair modificado", "Cifrado Rail Fence", "Escítala"]
abecedario = "abcdefghijklmnñopqrstuvwxyz"

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
    print("El texto codificado con Cifrado César es:", codificando)

def cesarDec(decodificar, movimiento):
    decodificando = ""
    for letra in decodificar:
        if letra != " ":
            índice = (abecedario.find(letra) - movimiento) % len(abecedario)
            decodificando += abecedario[índice]
        else:
            decodificando += letra
    print()
    print("El texto decodificado con Cifrado César es:", decodificando)

#Monoalfabetico codificación y decodificación.

def monoCod(texto, palabra):
    """
    -Subrutina-
    Codificación monoalfabético con palabra clave
    -Procedimiento-
    se crea el abecedario cifrado segun la palabra clave, y luego el texto se cambia de posicion
    numerica con la del abecedario cifrado para crear el texto cifrado
    -Entradas y Restricciones-
    El texto: Sin restricciones 
    
    -Salidas-
    El texto codificado en monoalfabético con palabra clave
    
    -Autores-
    
    Jeremy Matarrita Hernández 
    Andrey Morales Reyes 
    Alexei Quesada Leandro
    
    """
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
    print("El texto codificado con Cifrado Monoalfabético es: " + texto_cifrado)

def monoDec(texto, palabra):
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
    print("El texto decodificado con Cifrado Monoalfabético es: " + texto_descifrado)

#Vigenere codificación y decodificación.

def vigenereCod(texto,palabra):
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
    delimitador = "" 
    mensajeFinal = delimitador.join(cifrado)
    print("El texto codificado con Cifrado Vigenère es:",mensajeFinal)

def vigenereDec(texto,palabra):
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
    delimitador = "" 
    mensajeFinal = delimitador.join(cifrado)
    print("El texto decodificado con Cifrado Vigenère es:",mensajeFinal)

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
    print("El texto codificado con Cifrado PlayFair es:", codificar)

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
    print("El texto decodificado con Cifrado PlayFair es:", decodificando)

#Railfence codificación y decodificación.

def railfenceCod(texto):
     """
    -Subrutina-
    Codificación RailFencee
    -Procedimiento-
    Divide el texto en 3 partes y lo cifra con el abecedario especial segun la palabra,
    luego lo une y lo separa en grupos de 5
    -Entradas y Restricciones-
    El texto: Sin restricciones 
    
    -Salidas-
    El texto codificado en RailFence

    -Autores-
    
    Jeremy Matarrita Hernández 
    Andrey Morales Reyes 
    Alexei Quesada Leandro
    
    """

    arriba = ""
    medio = ""
    abajo = ""   
    while len(texto) % 4 != 0:
        texto += " "
    texto = texto.replace(" ", "-")
    for posicion, letra in enumerate(texto):
        posicion_cifrada = posicion % 4
        if posicion_cifrada == 0:
            arriba += letra
        elif posicion_cifrada == 1 or posicion_cifrada == 3:
            medio += letra
        elif posicion_cifrada == 2:
            abajo += letra          
    texto_cifrado = arriba + medio + abajo
    cifrado_completo = ""
    for posicion, letra in enumerate(texto_cifrado):
        cifrado_completo += letra
        if (posicion + 1) % 5 == 0:
            cifrado_completo += " "
    while cifrado_completo[-1] == " ":
        cifrado_completo = cifrado_completo[: -1]
    print("El texto codificado con Cifrado RailFence es:", cifrado_completo)
    
def railfenceDec(texto):
    """
    -Subrutina-
    Decodificación RailFencee
    -Procedimiento-
    deshace los grupos de 5, calcula las cantidades por línea, se separa en 3 lineas,
    ,se reconstruye el zigzag del cifrado y se cambian las líneas por espacios
    -Entradas y Restricciones-
    El texto: Sin restricciones 
    
    -Salidas-
    El texto decodificado en RailFence

    -Autores-
    
    Jeremy Matarrita Hernández 
    Andrey Morales Reyes 
    Alexei Quesada Leandro
    
    """
    texto = texto.replace(" ", "")
    distancia = len(texto)
    lineas = distancia // 4
    cantidad_arriba = lineas
    cantidad_abajo = lineas
    cantidad_medio = lineas * 2
    arriba = texto[:cantidad_arriba]
    medio = texto[cantidad_arriba : cantidad_arriba + cantidad_medio]
    abajo = texto[cantidad_arriba + cantidad_medio :]
    indice_arriba = 0
    indice_medio = 0
    indice_abajo = 0
    texto_descifrado = ""
    for posicion in range(distancia):
        posicion_cifrada = posicion % 4
        if posicion_cifrada == 0:
            texto_descifrado += arriba[indice_arriba]
            indice_arriba += 1
        elif posicion_cifrada == 1 or posicion_cifrada == 3:
            texto_descifrado += medio[indice_medio]
            indice_medio += 1
        elif posicion_cifrada == 2:
            texto_descifrado += abajo[indice_abajo]
            indice_abajo += 1
    texto_descifrado = texto_descifrado.replace("-", " ")
    while texto_descifrado[-1] == " ":
        texto_descifrado = texto_descifrado[:-1]
    print("El texto decodificado con Cifrado RailFence es:", texto_descifrado)

#Escitala codificación y decodificación.

def escitalaCod(texto, vueltas):
    texto = texto.replace(" ","-")
    while len(texto) % vueltas != 0:
        texto = texto +"-"
    matriz = []
    delimitador = ""
    for i in range(vueltas):
        texto1 = list(texto[i::vueltas])
        pedazos = delimitador.join(texto1)
        matriz.append(pedazos)
    mensajeFinal = delimitador.join(matriz)
    print("El texto codificado con Escítala es:", mensajeFinal)

def escitalaDec(texto, vueltas):
    texto = texto.replace(" ","")
    matriz= []
    mensajeFinal = []
    delimitador =""
    c = 0
    d = len(texto)//vueltas
    if len(texto)% vueltas == 0:
        for i in range(vueltas):
            matriz.append(texto[c:d])
            c = d
            d = d+len(texto)//vueltas
        for i in range(len(matriz[0])):
            for c in range(vueltas):
                mensajeFinal.append(matriz[c][i])
        mensajeFinal = delimitador.join(mensajeFinal)
        mensajeFinal = mensajeFinal.replace("-"," ")       
        print("El texto decodificado con Escítala es:", mensajeFinal)
    else:
        print("El texto no puede descodificarse.")

def valorarRestriccionesPalabra(palabra, decisión):
    if type(palabra) != str or any(letra not in abecedario for letra in palabra):
        raise Exception("La palabra clave no puede tener números, símbolos ni espacios.")

def valorarRestriccionesTexto(texto, decisión):
    if decisión == "4":
        if any(letra not in abecedario + "123 " for letra in texto):
            raise Exception("El texto no puede tener símbolos o números diferentes a 1, 2 y 3.")
    if decisión in ("5", "6"):
        if any(letra not in abecedario + "ABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ- " for letra in texto):
            raise Exception("El texto no puede tener símbolos ni números")
    else:
        if any(letra not in abecedario + " " for letra in texto):
            raise Exception("El texto no puede tener símbolos ni números")

def prepararTexto(frase, decisión):
    """Función que prepara el texto a codificar o decodificar.
    Entradas y restricciones:
    - decisión: Elección de tipo de cifrado del usuario a utilizar: Sin restricciones.
    - frase: Mensaje que el usuario desea codificar o decodificar: debe ser un conjunto de letras.
    Salidas:
    Retorna el texto sin tildes y mayúsculas para los tipos de cifrados
    que lo necesitan y elimina espacios extra en el texto.
    Autores:
    Jeremy Matarrita Hernández
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
    if decisión not in ("5", "6"):
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
    else:
        texto = frase
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
    - decisión: Elección de tipo de cifrado del usuario a utilizar: Sin restricciones.
    Salidas:
    Retorna True si el usuario escribe "S", False si no.
    Autores:
    Jeremy Matarrita Hernández
    Andrey Morales Reyes
    Alexei Quesada Leandro"""
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
    Programa principal de los tipos de cifrados
    Entradas y restricciones:
    - decisión: Elección de tipo de cifrado del usuario a utilizar: debe ser entero entre 1 y 7.
    - opción: Elección del usuario para codificar o decodificar: debe ser entero entre 1 y 2.
    - desplazamiento: Número de movimientos para el cifrado César: debe ser entero.
    - líneas: Número de caras para la figura de Escítala: debe ser entero menor o igual a 2.
    - texto: Mensaje que el usuario desea codificar o decodificar: debe ser un conjunto de letras.
    - palabra: Palabra clave que se utiliza en el cifrado Monoalfabético, Vigenère, y PlayFair
    para la codificación y decodificación del texto: debe ser un conjunto de letras.
    Salidas:
    Mensaje final al dejar de utilizar el programa.
    Autores:
    Jeremy Matarrita Hernández
    Andrey Morales Reyes
    Alexei Quesada Leandro
    """
    try:
        global abecedario
        global cifrado
        print("¡Buen día usuario!")
        print("Bienvenido al sistema de codificación y decodificación.")
        print("Aqui podrá codificar un mensaje en el cifrado que desee.")
        print("Tambien puede decodificar un mensaje con el tipo de decifrado correspondiente.")
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
                texto = prepararTexto(texto, decisión)
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
                if decisión == "6":
                    try:
                        líneas = int(input("Ingrese la cantidad de caras que tiene la figura: "))
                    except ValueError:
                        raise Exception("El valor de las vueltas debe ser un número entero.")
                        if líneas <= 1:
                            raise Exception("El número de caras que debe tener la figura debe ser mínimo de 2 y no puede ser un número negativo.")
                if opción == "1":
                    if decisión == "1":
                        #Subrutina Codificación Cifrado César
                        cesarCod(texto, desplazamiento)
                    if decisión == "2":
                        monoCod(texto, palabra)
                    if decisión == "3":
                        vigenereCod(texto, palabra)
                    if decisión == "4":
                        playfairCod(texto, palabra)
                    if decisión == "5":
                        railfenceCod(texto)
                    if decisión == "6":
                        escitalaCod(texto, líneas)
                if opción == "2":
                    if decisión == "1":
                        #Subrutina Decodificación Cifrado César
                        cesarDec(texto, desplazamiento)
                    if decisión == "2":
                        monoDec(texto, palabra)
                    if decisión == "3":
                        vigenereDec(texto, palabra)
                    if decisión == "4":
                        playfairDec(texto, palabra)
                    if decisión == "5":
                        railfenceDec(texto)
                    if decisión == "6":
                        escitalaDec(texto, líneas)
                continuar = usarNuevamente(decisión)
            else:
                continuar = False
        print()
        print("Gracias por utilizar este programa :)")
    except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
  main()

#Cesar codificación y decodificación.

def cesarCod(texto, desplazamiento):

def cesarDec(texto, desplazamiento):

#Monoalfabetico codificación y decodificación.

def monoCod(texto,palabra):

def monoDec(texto,palabra):

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
    return mensajeFinal

def vigenereDec(texto,palabra):

#Playfair codificación y decodificación.

def playfairCod(codificar, código):
    #Preparación de palabra clave
    abecedario = ("abcdefghijklmnñopqrstuvwxyz123")
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
    #Separación de cada palabra del texto a codificar en dos letras
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
    print("El texto cifrado con PlayFair es:", codificar)

def playfairDec(decodificar, código):
    #Restricciones
    verificar = ""
    for letra in decodificar:
        if letra == verificar:
            raise Exception("El texto a decodificar no puede tener dos letras iguales seguidas.")
        verificar = letra
    decodificar = decodificar.split(" ")
    for i in range(0, len(decodificar)):
        if len(decodificar[i]) % 2 != 0:
            raise Exception("Todas las palabras del texto a decodificar deben tener una cantidad de letras par.")
    #Preparación de palabra clave
    abecedario = ("abcdefghijklmnñopqrstuvwxyz123")
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
    print("El texto cifrado con PlayFair es:", decodificando)

#Railfence codificación y decodificación.

def railfenceCod(texto):

def railfenceDec(texto):

#Escitala codificación y decodificación.

def escitalaCod(texto, lineas):

def escitalaDec(texto, lineas):

#Programa principal  

def main():

def prepararTexto(frase):
    while frase[-1] == " ":
        frase = frase[: -1]
    abecedario = ("abcdefghijklmnñopqrstuvwxyz123 ")
    if type(frase) != str or any(letra not in abecedario for letra in frase):
        raise Exception("El texto no puede tener símbolos o números diferentes a 1, 2 y 3.")
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
    abecedario = ("abcdefghijklmnñopqrstuvwxyz")
    if type(clave) != str or any(letra not in abecedario for letra in clave):
        raise Exception("La palabra clave no puede tener números, símbolos ni espacios.")
    código = ""
    for letra in clave.lower():
        if letra not in código:
            código += letra
    return código

def usarNuevamente():
    """Función que le pregunta al usuario si desea utilizar de nuevo el programa. Sólo acepta "S" o "N" como respuesta.
    Entradas y restricciones:
    - Ninguna.
    Salidas:
    Retorna True si el usuario escribe "S", False si no."""
    print()
    respuesta = input("¿Desea utilizar de nuevo el programa? (S/N) ")
    respuesta = respuesta.lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta inválida. Inténtelo nuevamente.")
        respuesta = input("¿Desea utilizar de nuevo el programa? (S/N) ")
        respuesta = respuesta.lower()
    return respuesta == "s"

  """
  Programa principal del Proyecto-0.
  """
  print("¡Buen día usuario!")
  print("Bienvenido al sistema de codificación y decodificación.")
  print("Aqui podrá codificar un mensaje en el cifrado que desee.")
  print("Tambien puede decodificar un mensaje con el tipo de decifrado que desee.")
  print("Tipos de cifrados disponibles:")
  print("1. Cifrado Cesar.")
  print("2. Cifrado Monoalfabético.")
  print("3. Cifrado Vigenère.")
  print("4. Cifrado Playfair modificado.")
  print("5. Cifrado Railfence.")
  print("6. Cifrado Escítala.")
  print("7. Salir del sistema.")
  try:
    continuar = True
    while continuar:
      decision = int(input("¿Que tipo de cifrado quiere utilizar el día de hoy?:"))
      if decision == 1:
        print("Gracias por escoger el cifrado Cesar.")
        print("¿Qué desea hacer ahora?") 
        print("1. Codificar un mensaje") 
        print("2. Decodificar un mensaje")
        decision = int(input("Escoja un valor entre 1 y 2"))
        if decision == 1:
          texto = str(input("Por favor, introduzca su mensaje a codificar:"))
          print("Gracias por introducir su mensaje correctamente.")
          desplazamiento = int(input("Ahora, introduzca el desplazamiento:"))
          print("Gracias por introducir el desplazamiento correctamente.")
          print("Ahora, su mensaje cifrado es:", cesarCod(texto , desplazamiento))
        elif decision == 2:
          texto = str(input("Por favor, introduzca su mensaje codificado:"))
          print("Gracias por introducir su mensaje correctamente.")
          desplazamiento = int(input("Ahora, introduzca el desplazamiento:"))
          print("Gracias por introducir el desplazamiento correctamente.")
          print("Ahora, su mensaje decifrado es:", cesarDec(texto , desplazamiento))
      elif decision == 2:
        print("Gracias por escoger el cifrado Monoalfabético.")
        print("¿Qué desea hacer ahora?") 
        print("1. Codificar un mensaje") 
        print("2. Decodificar un mensaje")
        decision = int(input("Escoja un valor entre 1 y 2"))
        if decision == 1:
          texto = str(input("Por favor, introduzca su mensaje a codificar:"))
          print("Gracias por introducir su mensaje correctamente.")
          palabra = srt(input("Ahora, introduzca la palabra clave:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje cifrado es:", monoCod(texto , palabra))
        elif decision == 2:
          texto = str(input("Por favor, introduzca su mensaje codificado:"))
          print("Gracias por introducir su mensaje correctamente.")
          palabra = srt(input("Ahora, introduzca la palabra clave:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje decifrado es:", monoDec(texto , palabra))
      elif decision == 3:
        print("Gracias por escoger el cifrado Vinegère.")
        print("¿Qué desea hacer ahora?") 
        print("1. Codificar un mensaje") 
        print("2. Decodificar un mensaje")
        decision = int(input("Escoja un valor entre 1 y 2"))
        if decision == 1:
          texto = str(input("Por favor, introduzca su mensaje a codificar:"))
          print("Gracias por introducir su mensaje correctamente.")
          palabra = srt(input("Ahora, introduzca la palabra clave:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje cifrado es:", vinegereCod(texto , palabra))
        elif decision == 2:
          texto = str(input("Por favor, introduzca su mensaje codificado:"))
          print("Gracias por introducir su mensaje correctamente.")
          palabra = str(input("Ahora, introduzca la palabra clave:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje decifrado es:", vinegereDec(texto , palabra))
      elif decision == 4:
        print("Gracias por escoger el cifrado Playfair.")
        print("¿Desea codificar o decodificar?")
        print("1. Codificar.")
        print("2. Decodificar.")
        opción = input("Su opción: ")
        while opción not in ("1", "2"):
            print("Opción no válida")
            opción = input("Su opción: ")
        if opción == "1":
            mensaje = "codificar"
        if opción == "2":
            mensaje = "decodificar"
        print("Gracias por introducir su opción correctamente.")
        #Texto a codificar o decodificar
        texto = str(input(f"Ingrese el texto que desea {mensaje}: "))
        texto = prepararTexto(texto)
        #Palabra clave
        palabra = str(input("ingrese el palabra clave utilizada en la codificación: "))
        palabra = prepararPalabra(palabra)
        if opción == "1":
            playfairCod(texto, palabra)
        if opción == "2":
            playfairDec(texto, palabra)
      elif decision == 5:
        print("Gracias por escoger el cifrado Railfence.")
        print("¿Qué desea hacer ahora?") 
        print("1. Codificar un mensaje") 
        print("2. Decodificar un mensaje")
        decision = int(input("Escoja un valor entre 1 y 2"))
        if decision == 1:
          texto = str(input("Por favor, introduzca su mensaje a codificar:"))
          print("Gracias por introducir su mensaje correctamente.")
          print("Ahora, su mensaje cifrado es:", railfenceCod(texto))
        elif decision == 2:
          texto = str(input("Por favor, introduzca su mensaje codificado:"))
          print("Gracias por introducir su mensaje correctamente.")
          print("Ahora, su mensaje decifrado es:", railfenceDec(texto))
      elif decision == 6:
        print("Gracias por escoger el cifrado Escítala.")
        print("¿Qué desea hacer ahora?") 
        print("1. Codificar un mensaje") 
        print("2. Decodificar un mensaje")
        decision = int(input("Escoja un valor entre 1 y 2"))
        if decision == 1:
          texto = str(input("Por favor, introduzca su mensaje a codificar:"))
          print("Gracias por introducir su mensaje correctamente.")
          lineas = int(input("Ahora, introduzca las líneas:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje cifrado es:", escitalaCod(texto , lineas))
        elif decision == 2:
          texto = str(input("Por favor, introduzca su mensaje codificado:")
          print("Gracias por introducir su mensaje correctamente.")
          lineas = int(input("Ahora, introduzca las líneas:"))
          print("Gracias por introducir la palabra clave correctamente.")
          print("Ahora, su mensaje decifrado es:", escitalaDec(texto , lineas))
        continuar = usarNuevamente()
    print("Gracias por utilizar el software, que tenga lindo día.")
  except Exception as e:
    print(f"ERROR: {e}")

if __name__ == "__main__":
  main()

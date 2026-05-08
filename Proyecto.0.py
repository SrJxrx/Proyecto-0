#Cesar codificación y decodificación.

def cesarCod(texto, desplazamiento):

def cesarDec(texto, desplazamiento):

#Monoalfabetico codificación y decodificación.

def monoCod(texto,palabra):

def monoDec(texto,palabra):

#Vigenere codificación y decodificación.

def vigenereCod(texto,palabra):

def vigenereDec(texto,palabra):

#Playfair codificación y decodificación.

def playfairCod(texto,palabra):

def playfairDec(texto,palabra):

#Railfence codificación y decodificación.

def railfenceCod(texto):

def railfenceDec(texto):

#Escitala codificación y decodificación.

def escitalaCod(texto, lineas):

def escitalaDec(texto, lineas):

def main():
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
  print("6. Cifrado Escitala.")
  print("7. Salir del sistema.")
  decision = int(input("¿Que tipo de cifrado quiere utilizar el día de hoy?:")
  if decision == 1:
    print("Gracias por escoger el cifrado Cesar.")
    print("¿Qué desea hacer ahora?") 
    print("1. Codificar un mensaje") 
    print("2. Decodificar un mensaje")
    decision = int(input("Escoja un valor entre 1 y 2")
    if decision == 1:
      texto = str(input("Por favor, introduzca su mensaje a codificar:")
      print("Gracias por introducir su mensaje correctamente.")
      desplazamiento = int(input("Ahora, introduzca el desplazamiento:")
      print("Gracias por introducir el desplazamiento correctamente.")
      print("Ahora, su mensaje cifrado es:", cesarCod(texto , desplazamiento))
    elif decision == 2:
      texto = str(input("Por favor, introduzca su mensaje codificado:")
      print("Gracias por introducir su mensaje correctamente.")
      desplazamiento = int(input("Ahora, introduzca el desplazamiento:")
      print("Gracias por introducir el desplazamiento correctamente.")
      print("Ahora, su mensaje decifrado es:", cesarDec(texto , desplazamiento))
  elif decision == 2:
    print("Gracias por escoger el cifrado Monoalfabético.")
    print("¿Qué desea hacer ahora?") 
    print("1. Codificar un mensaje") 
    print("2. Decodificar un mensaje")
    decision = int(input("Escoja un valor entre 1 y 2")
    if decision == 1:
      texto = str(input("Por favor, introduzca su mensaje a codificar:")
      print("Gracias por introducir su mensaje correctamente.")
      palabra = int(input("Ahora, introduzca la palabra clave:")
      print("Gracias por introducir la palabra clave correctamente.")
      print("Ahora, su mensaje cifrado es:", monoCod(texto , palabra))
    elif decision == 2:
      texto = str(input("Por favor, introduzca su mensaje codificado:")
      print("Gracias por introducir su mensaje correctamente.")
      desplazamiento = int(input("Ahora, introduzca la palabra clave:")
      print("Gracias por introducir la palabra clave correctamente.")
      print("Ahora, su mensaje decifrado es:", monoDec(texto , palabra))
  elif decision == 3:
    print("Gracias por escoger el cifrado Vinegère.")
    print("¿Qué desea hacer ahora?") 
    print("1. Codificar un mensaje") 
    print("2. Decodificar un mensaje")
    decision = int(input("Escoja un valor entre 1 y 2")
    if decision == 1:
      texto = str(input("Por favor, introduzca su mensaje a codificar:")
      print("Gracias por introducir su mensaje correctamente.")
      palabra = int(input("Ahora, introduzca la palabra clave:")
      print("Gracias por introducir la palabra clave correctamente.")
      print("Ahora, su mensaje cifrado es:", vinegereCod(texto , palabra))
    elif decision == 2:
      texto = str(input("Por favor, introduzca su mensaje codificado:")
      print("Gracias por introducir su mensaje correctamente.")
      desplazamiento = int(input("Ahora, introduzca la palabra clave:")
      print("Gracias por introducir la palabra clave correctamente.")
      print("Ahora, su mensaje decifrado es:", vinegereDec(texto , palabra))
                           
                   
                 
if __name__ == "__main__":
  main()

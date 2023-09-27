#paso 1: creacion de las funciones
def suma(x, y):
  return x + y
def resta(x, y):
  return x - y
def multiplicacion(x, y):
  return x * y
def division(x, y):
  try:
     return x / y
  except Exception:
    print("No se ha podido realizar la división")
def raiz_cuadrada(x):
  return x ** 0.5
def potencia(x):
  return x ** x
#paso 2: funcion principal
def calculadora():
    continuar = True
    while continuar:
      opciones = ['suma', 'resta', 'multiplicacion', 'division', 'raiz cuadrada', 'potencia']
      print(opciones)
      elegir_operacion = str(input("Elige una de las opciones de arriba O bien escribe 'salir' para salir de la calculadora: "))
      if elegir_operacion == "salir":
          continuar = False
          print("Hasta pronto")
      elif elegir_operacion not in opciones:
          print("Esta no es una opción valida")
      elif elegir_operacion in opciones:
        numero1 = float(input("Introduce un número: "))
        if elegir_operacion == "suma":
          numero2 = float(input("Introduce otro número: "))
          solucion = suma(numero1, numero2)
          print(f"la {elegir_operacion} de {numero1} y {numero2} es igual a: {solucion}")
        elif elegir_operacion == "resta":
          numero2 = float(input("Introduce otro número: "))
          solucion = resta(numero1, numero2)
          print(f"la {elegir_operacion} de {numero1} y {numero2} es igual a: {solucion}")
        elif elegir_operacion == "multiplicacion":
          numero2 = float(input("Introduce otro número: "))
          solucion = multiplicacion(numero1, numero2)
          print(f"la {elegir_operacion} de {numero1} y {numero2} es igual a: {solucion}")
        elif elegir_operacion == "division":
          numero2 = float(input("Introduce otro número: "))
          solucion = division(numero1, numero2)
          print(f"la {elegir_operacion} de {numero1} y {numero2} es igual a: {solucion}")
        elif elegir_operacion == "raiz cuadrada":
          solucion = raiz_cuadrada(numero1)
          print(f"la {elegir_operacion} de {numero1} es igual a: {solucion}")
        elif elegir_operacion == "potencia":
          solucion = potencia(numero1)
          print(f"la {elegir_operacion} de {numero1} es igual a: {solucion}")
calculadora()
#paso 3: seguir operando con la {solucion} y no con un nuevo numero
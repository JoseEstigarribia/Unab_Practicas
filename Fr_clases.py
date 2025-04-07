import random
import time

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar(self, otra):
        num = self.numerador * otra.denominador + otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def restar(self, otra):
        num = self.numerador * otra.denominador - otra.numerador * self.denominador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def multiplicar(self, otra):
        num = self.numerador * otra.numerador
        den = self.denominador * otra.denominador
        return Fraccion(num, den)

    def dividir(self, otra):
        num = self.numerador * otra.denominador
        den = self.denominador * otra.numerador
        return Fraccion(num, den)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

# Generar fracciones aleatorias como objetos
def generar_fracciones_clase(cantidad):
    return [Fraccion(random.randint(1, 10), random.randint(1, 10)) for _ in range(cantidad)]

# Ejecución con cálculo del tiempo
inicio = time.time()
fracciones_clase = generar_fracciones_clase(100000)
resultado_clase = fracciones_clase[0].sumar(fracciones_clase[1])  # Ejemplo con dos fracciones
fin = time.time()

print(f"Resultado de suma (Fr con clases): {resultado_clase}")
print(f"Tiempo de ejecución (Fr con clases): {fin - inicio:.2f} segundos")

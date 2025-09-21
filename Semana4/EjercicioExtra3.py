# **Convertidor de unidades de temperatura**
#    - Pida al usuario ingresar una temperatura en Celsius
#    - Conviértala a Fahrenheit y Kelvin
#    - Muestre los tres valores
from fractions import Fraction

celsius_temp = int(input("Ingrese la temperatura en Celsius: "))
fahren_temp = (celsius_temp * Fraction(9,5)) + 32
kelvin_temp = celsius_temp + 273.15

print(f"La temperatura en Celsius es: {celsius_temp}")
print(f"La temperatura en Fahrenheit es: {fahren_temp}")
print(f"La temperatura en Kelvin es: {kelvin_temp}")
''' Ejercicio 1: Pintar cuadrado
    - Preguntar por tamaño de cuadrado.
    - Crear función que os pinte cuadrado usando por defecto *
    - Poder pasar otro símbolo para pintar el cuadrado.
'''

def paint_square(size, symbol="*"):
    for i in range(size):
        if i == 0 or i == size-1:
            print(symbol * size)
        else:
            print(f"{symbol}{' ' * (size-2)}{symbol}")
    
        

paint_square(1)  
paint_square(5, "#")
print()
print("-"*20)
print("-"*20)  





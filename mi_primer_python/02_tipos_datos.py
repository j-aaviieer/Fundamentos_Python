#Ejercicio 2: Variables y tipos de datos
nombre = "Camila"
ciudad = "Santiago"
print(nombre)
print(ciudad)
print(type(nombre))

'''
Crear tres variables con el nombre de una pelicula,
un videojuego y una asignatura. Muestralas
con print() y aplica type() a una de ellas.
'''
pelicula = input("Ingrese el nombre de la pelicula: ")
juego = input("Ingrese el nombre del videojuego: ")
asignatura = input("Ingrese el nombre de la asignatura: ")

print(f'{juego} {pelicula} {asignatura}')

# 4.2 Enteros: int
edad = int(input("Ingresa tu edad: "))
cantidad_hermanos = int(input("Ingresa tu cantidad de hermanos: "))
año_actual = int(input("Ingresa el año actual: "))

print(edad)
print(cantidad_hermanos)
print(año_actual)
print(type(edad))

# 4.3 Decimales: float
precio_producto = float(input("Ingresa el precio del producto: "))
temperatura = float(input("Ingresa la temperatura: "))
promedio_notas = float(input("Ingresa tu promedio de notas: "))

print(precio_producto)
print(temperatura)
print(promedio_notas)
print(type(precio_producto))
print(type(temperatura))

# 4.4 Booleanos: bool
tengo_internet = True
termine_tarea = True
tengo_clases_manana = False

print(tengo_internet)
print(termine_tarea)
print(tengo_clases_manana)
print(type(tengo_internet))

#Ejercicio 7 (4 Tipos en una ficha)
nombre_producto = str(input("Ingrese el nombre del producto...")) # str (Cadena de texto)
cantidad_stock = int(input("Ingresa la cantidad de stock...")) # int (Numeros enteros)
precio_unitario = float(input("Ingresa el precio unitario...")) # float (Numeros decimales)
disponible = True # bool (True o False)

print("Producto elegido")
print(nombre_producto, type(nombre_producto))
print(cantidad_stock, type(cantidad_stock))
print(precio_unitario, type(precio_unitario))
print(disponible, type(disponible))
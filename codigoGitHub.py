
compras = []
total_compra = 0
cont = 0
zapatos = {
    1: ["sandalias","negras", 10], 
    2: ["botas","negras", 15], 
    3: ["tenis","blancos", 12], 
    4: ["tenis","rojos", 12]
}
jeans = {
    1: ["clásico", "azul", 20], 
    2: ["clásico", "negro", 20], 
    3: ["con desgastes", "azul", 15], 
    4: ["con desgastes", "gris", 15]
}
camisetas = {
    1: ["polo", "blanca", "20"], 
    2: ["polo", "azul", "20"], 
    3: ["cuello V", "negra", "15"], 
    4: ["cuello V", "lila", "15"]
}

print("ingrese los siguientes datos")
nombres = input("ingrese nombres y apellidos: ")
while True:
    try:
        id = int(input("ingrese su numero de identificación: "))
    except ValueError:
        print("por favor ingrese valores numéricos y sin espacios")
        continue
    break

direccion = input("ingrese su direccion: ")
while True:
    try:
        telefono = int(input("ingrese su numero de telefono celular: "))
    except ValueError:
            print("por favor ingrese valores numéricos y sin espacios")
            continue
    break

while True:
    print("'\ningrese el articulo que desea llevar: ")
    menu = input("1. camisetas\n2. jeans\n3. zapatos\n")
    if menu == "1":
        articulos = camisetas
    elif menu == "2":
        articulos = jeans
    elif menu == "3":
        articulos = zapatos
    else:
        print("opcion de producto no válida, ingrese nuevamente ")
        continue      
    print("articulos disponibles")
    for clave, producto in articulos.items():
        print(f"{clave}: {producto[0]} - {producto[1]} - ${producto[2]}")
    opcion = int(input("Seleccione un producto: "))
    if opcion in articulos:
        cont += 1
        if cont <= 3:
            compras.append(articulos[opcion])
            total_compra += articulos[opcion][2]                                 
        else:
            break
    else:
        break 

print("\nDetalle de la compra:")
for i in compras:
    print(f"Producto: {i[0]}, Color: {i[1]}, Precio: ${i[2]}")
print(f"Total de la compra: ${total_compra}")




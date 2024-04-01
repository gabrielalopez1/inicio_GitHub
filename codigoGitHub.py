
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



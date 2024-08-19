class Cuadernos:
    __marca = ""
    hojas = 0
    tipoHojas = ""
    encuadernado = ""
    tamaño = ""
    precio = 0
    precioVenta = 0
    __multPrecio = 0

    def __init__(self):
        self.__marca = "HOJITAS"
        self.__multPrecio = 1.3
    
    def marca(self):
        return self.__marca
    
    def multPrecio(self):
        return self.__multPrecio
    
class Lapices:
    __marcaLp = ""
    cantidad = 0
    tamaño = ""
    tipo = ""
    material = ""
    precio = 0
    precioVenta = 0
    __multPrecio = 0
    
    def __init__(self):
        self.__marcaLp = "RAYAS"
        self.__multPrecio = 1.3
    
    def marcaLapices(self):
        return self.__marcaLp
    
    def multPrecio(self):
        return self.__multPrecio
    
def pasarDatosLapices(lapices, cantidadLp, tamañoLp, tipoLp, materialLp, precioLp):
    lapices.cantidad = cantidadLp
    lapices.tamaño = tamañoLp
    lapices.tipo = tipoLp
    lapices.material = materialLp
    lapices.precio = precioLp
    lapices.precioVenta = lapices.multPrecio() * precioLp
    
def obtenerDatosLapices(lapices):
    print(f"************ Ingresar Datos *************")

    cantidadLp = int(input("Cantidad de Lápices por paquete: "))
    tamañoLp = input("Tamaño de los lápices: ")
    while True:
        tipoLp = input("Tipo de Lápices (color o grafito): ").lower()
        if tipoLp in ["color", "grafito"]:
            break
        else:
            print("Error, respuesta no válida, ingrese 'color' o 'grafito'.")
    
    materiales_validos = ["madera", "plástico", "acero", "resina"]
    while True:
        materialLp = input(f"Material (Opciones: {', '.join(materiales_validos)}): ").lower()
        if materialLp in materiales_validos:
            break
        else:
            print(f"Error, respuesta no válida, ingrese una de las siguientes opciones: {', '.join(materiales_validos)}.")
    
    precioLp = float(input("Precio del producto: $"))
    pasarDatosLapices(lapices, cantidadLp, tamañoLp, tipoLp, materialLp, precioLp)
    
def mostrarDatosLapices(lapices):
    print(f"************ *************")
    print("Tipo: Lápices")
    print(f"Marca: {lapices.marcaLapices()}")
    print(f"Cantidad: {lapices.cantidad}")
    print(f"Tamaño: {lapices.tamaño}")
    print(f"Tipo: {lapices.tipo}")
    print(f"Material: {lapices.material}")
    print(f"Precio Venta: ${lapices.precioVenta}")
    
    
def pasarDatosCuadernos(cuadernos, numHojas, tipoHojasC, encuadernadoC, tamañoC, precioCompra):
    cuadernos.hojas = numHojas
    cuadernos.tipoHojas = tipoHojasC
    cuadernos.encuadernado = encuadernadoC
    cuadernos.tamaño = tamañoC
    cuadernos.precio = precioCompra
    cuadernos.precioVenta = precioCompra * cuadernos.multPrecio()

def obtenerDatosCuadernos(cuadernos):
    print("************ Ingresar Datos *************")

    while True:
        numHojas = int(input("Número de Hojas (50 / 100): "))
        if numHojas in [50, 100]:
            break
        else: 
            print("Error, número de hojas no válido")
    while True:
        tipoHojasC = input("Tipo de Hoja (Rayado, Cuadriculado, Liso, Doble Raya): ").lower()
        if tipoHojasC in ["rayado", "cuadriculado", "liso", "doble raya"]:
            break
        else:
            print("Error, respuesta no válida, ingrese 'Rayado', 'Cuadriculado', 'Liso' o 'Doble Raya'.")
    while True:
        encuadernadoC = input("Encuadernado (Anillado/Cosido): ").lower()
        if encuadernadoC in ["anillado", "cosido"]:
            break
        else:
            print("Error, respuesta no válida, ingrese 'Anillado' o 'Cosido'.")
    tamañoC = input("Tamaño del Cuaderno: ")
    precioCompra = float(input("Precio de Compra: $"))
    pasarDatosCuadernos(cuadernos, numHojas, tipoHojasC, encuadernadoC, tamañoC, precioCompra)
    
def mostrarDatosCuadernos(cuadernos):
    print(f"************ *************")
    print("Tipo: Cuaderno")
    print(f"Marca: {cuadernos.marca()}")
    print(f"Número de Hojas: {cuadernos.hojas}")
    print(f"Tipo de Hojas: {cuadernos.tipoHojas}")
    print(f"Encuadernado: {cuadernos.encuadernado}")
    print(f"Tamaño: {cuadernos.tamaño}")
    print(f"Precio de Venta: ${cuadernos.precioVenta}")


#--------------------Iniciar Programa-----------------------------
print("************************")
print("Sistema inventario")

cuadernos_comprados = []
lapices_comprados = []

while True:
    print("Escoja una Opción")
    while True:
        opt = input("Ingrese 'cuadernos' para Cuadernos o 'lapices' para Lápices: ").lower()
        if opt in ["cuadernos", "lapices"]:
            break
        else:
            print("Opción inválida, por favor ingrese 'cuadernos' o 'lapices'.")

    if opt == "cuadernos":
        cuaderno = Cuadernos()
        obtenerDatosCuadernos(cuaderno)
        cuadernos_comprados.append(cuaderno)
    
    elif opt == "lapices":
        lapiz = Lapices()
        obtenerDatosLapices(lapiz)
        lapices_comprados.append(lapiz)
    
    while True:
        opt = input("¿Desea continuar el chequeo? (si/no): ").lower()
        if opt in ["si", "no"]:
            break
        else:
            print("Respuesta inválida, por favor ingrese 'si' o 'no'.")
    
    if opt == "no":
        break

# Mostrar factura al finalizar
print("\n******* resumen *******")
for cuaderno in cuadernos_comprados:
    mostrarDatosCuadernos(cuaderno)

for lapiz in lapices_comprados:
    mostrarDatosLapices(lapiz)

print("************************")
print("Fin del programa")

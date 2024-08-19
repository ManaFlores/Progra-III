class Vehiculo:
    origen = ""
    __capacidad = 5
    __ruedas = 4
    marca = ""
    modelo = ""
    color = ""
    categoria = ""
    transmision = ""
    numeroDePuertas = 0
    tipoCombustible = ""
    precioCompra = 0
    precioVenta = 0
    __multiplicadorVenta = 1.4

    def __init__(self):
        self.__capacidad = 5
        self.__ruedas = 4
        self.__multiplicadorVenta = 1.4
    
    def capacidad(self):
        return self.__capacidad
        
    def ruedas(self):
        return self.__ruedas
    
    def multiplicadorVenta(self):
        return self.__multiplicadorVenta


def pasarDatos(vehiculo, origenPais, marcaVh, modeloVh, colorVh, categoriaVh, transmisionVh, numeroDePuertas, tipoCombustible, precioDelVh):
    vehiculo.origen = origenPais
    vehiculo.marca = marcaVh
    vehiculo.modelo = modeloVh
    vehiculo.color = colorVh
    vehiculo.categoria = categoriaVh
    vehiculo.transmision = transmisionVh
    vehiculo.numeroDePuertas = numeroDePuertas
    vehiculo.tipoCombustible = tipoCombustible
    vehiculo.precioCompra = precioDelVh
    vehiculo.precioVenta = vehiculo.multiplicadorVenta() * vehiculo.precioCompra


def obtenerDatos(vehiculo):
    print("********* Ingresar Datos *************")
    
    while True:
        origenPais = input("Origen (L: Local / I: Importado): ").lower()
        if origenPais == "l":
            origenPais = "Local"
            break
        elif origenPais == "i":
            origenPais = "Importado"
            break
        else:
            print("Respuesta no válida, ingrese L o I")
    
    marcaVh = input("Marca: ")
    modeloVh = input("Modelo: ")
    colorVh = input("Color: ")
    
    categorias = ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible", "Pickup", "Van"]
    print("\nSeleccione la categoría del vehículo:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            opcionCategoria = int(input("\nIngrese el número de la categoría: "))
            if 1 <= opcionCategoria <= len(categorias):
                categoriaVh = categorias[opcionCategoria - 1]
                break
            else:
                print("Opción no válida. Por favor, seleccione un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    while True:
        transmisionVh = input("Transmisión del Vehículo (Manual/Automática): ").capitalize()
        if transmisionVh in ["Manual", "Automática", "Automatica"]:
            transmisionVh = "Automática"
            break
        else:
            print("Respuesta no válida, ingrese Manual o Automática.")
    
    while True:
        try:
            numeroDePuertas = int(input("Número de Puertas: "))
            if numeroDePuertas > 0:
                break
            else:
                print("Número de puertas no válido.")
        except ValueError:
            print("Por favor ingrese un número válido para el número de puertas.")
    
    tiposCombustible = ["Gasolina", "Diésel", "Eléctrico", "Híbrido"]
    while True:
        tipoCombustible = input("Tipo de Combustible (Gasolina, Diésel, Eléctrico, Híbrido): ").capitalize()
        if tipoCombustible in tiposCombustible:
            break
        else:
            print(f"Tipo de combustible no válido. Las opciones válidas son: {', '.join(tiposCombustible)}.")
    
    precioDelVh = float(input("Ingrese el precio de compra: $"))
    
    pasarDatos(vehiculo, origenPais, marcaVh, modeloVh, colorVh, categoriaVh, transmisionVh, numeroDePuertas, tipoCombustible, precioDelVh)


def mostrarDatos(vehiculo):
    print("""
   ---------------------------.
 `/""""/""""/|""|'|""||""|   ' \.
 /    /    / |__| |__||__|      |
/----------=====================|
| \  /V\  /    _.               |
|()\ \W/ /()   _            _   |
|   \   /     / \          / \  |-( )
=C========C==_| ) |--------| ) _/==] _-(__)
 \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.""")
    
    print(f"- Origen: {vehiculo.origen}")
    print(f"- Marca: {vehiculo.marca}")
    print(f"- Modelo: {vehiculo.modelo}")
    print(f"- Categoría: {vehiculo.categoria}")
    print(f"- Capacidad: {vehiculo.capacidad()} pasajeros")
    print(f"- Número de Ruedas: {vehiculo.ruedas()}")
    print(f"- Color: {vehiculo.color}")
    print(f"- Transmisión: {vehiculo.transmision}")
    print(f"- Número de Puertas: {vehiculo.numeroDePuertas}")
    print(f"- Tipo de Combustible: {vehiculo.tipoCombustible}")
    print(f"- Precio al Público: ${vehiculo.precioVenta:.2f}")



carro1 = Vehiculo()
obtenerDatos(carro1)
mostrarDatos(carro1)

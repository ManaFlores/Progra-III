class PropiedadAirbnb:
    tipo = ""
    tamaño = 0
    habitaciones = 0
    baños = 0
    aireAcondicionado = False
    piscina = False
    huespedesPermitidos = 0
    precioBase = 0
    precioVenta = 0

    def __init__(self):
        self.__multHuespedExtra = 1.05  # Aumento base del 5%
        self.__multAireOPiscina = 1.03  # Aumento adicional del 3% por aire acondicionado o piscina

    def calcularPrecioVenta(self):
        extra_huespedes = max(0, self.huespedesPermitidos - 5)
        # Calcula el aumento por huéspedes extra
        aumento_huespedes = self.__multHuespedExtra ** extra_huespedes
        # Calcula el aumento por aire acondicionado o piscina
        aumento_extra = self.__multAireOPiscina if self.aireAcondicionado or self.piscina else 1
        # Calcula el precio de venta total
        self.precioVenta = self.precioBase * aumento_huespedes * aumento_extra

def asignarDatos(propiedad, tipoProp, tamañoProp, habitacionesProp, bañosProp, aireAcondicionadoProp, piscinaProp, huespedesProp, precioBaseProp):
    propiedad.tipo = tipoProp
    propiedad.tamaño = tamañoProp
    propiedad.habitaciones = habitacionesProp
    propiedad.baños = bañosProp
    propiedad.aireAcondicionado = aireAcondicionadoProp
    propiedad.piscina = piscinaProp
    propiedad.huespedesPermitidos = huespedesProp
    propiedad.precioBase = precioBaseProp
    propiedad.calcularPrecioVenta()

def obtenerDatos(propiedad):
    print("***** Registro de Información de la Propiedad *****")
    tipoProp = input("Especifique el tipo de propiedad (Casa, Apartamento, Habitación, Chalet, Villa): ")
    tamañoProp = float(input("Ingrese el tamaño de la propiedad en metros cuadrados: "))
    habitacionesProp = int(input("Número de habitaciones: "))
    bañosProp = int(input("Número de baños: "))
    aireAcondicionadoProp = input("¿Posee aire acondicionado? (Sí/No): ").strip().lower() == "sí"
    piscinaProp = input("¿Posee piscina? (Sí/No): ").strip().lower() == "sí"
    huespedesProp = int(input("Número de huéspedes permitidos: "))
    precioBaseProp = float(input("Ingrese el precio base por noche: $"))

    asignarDatos(propiedad, tipoProp, tamañoProp, habitacionesProp, bañosProp, aireAcondicionadoProp, piscinaProp, huespedesProp, precioBaseProp)

def mostrarDatos(propiedad):
    print("********** Detalles de la Propiedad **********")
    print(f"Tipo de Propiedad: {propiedad.tipo}")
    print(f"Tamaño: {propiedad.tamaño} m²")
    print(f"Número de Habitaciones: {propiedad.habitaciones}")
    print(f"Número de Baños: {propiedad.baños}")
    print(f"Aire Acondicionado: {'Sí' if propiedad.aireAcondicionado else 'No'}")
    print(f"Piscina: {'Sí' if propiedad.piscina else 'No'}")
    print(f"Huespedes Permitidos: {propiedad.huespedesPermitidos}")
    print(f"Precio Base por Noche: ${propiedad.precioBase:.2f}")
    print(f"Precio de Venta por Noche: ${propiedad.precioVenta:.2f}")

def main():
    propiedades = []
    while True:
        propiedad = PropiedadAirbnb()
        obtenerDatos(propiedad)
        propiedades.append(propiedad)
        mostrarDatos(propiedad)
        
        continuar = input("¿Desea continuar registrando propiedades? (Sí/No): ").strip().lower()
        if continuar not in ["sí", "si"]:
            break

    print("\n********** Resumen de Propiedades Registradas **********")
    for i, propiedad in enumerate(propiedades, start=1):
        print(f"\nPropiedad {i}:")
        mostrarDatos(propiedad)

if __name__ == "__main__":
    main()

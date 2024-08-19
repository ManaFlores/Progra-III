class Dispositivos:
    tipo = ""
    __marca = ""
    modelo = ""
    precio = 0
    __multVenta = 0
    almacenamiento = 0
    ram = 0
    sistemaOperativo = ""
    resolucionCamara = ""
    conectividad = ""
    precioVenta = 0
    
    def __init__(self):
        self.__marca = "PHR"
        self.__multVenta = 1.7
    
    def marca(self):
        return self.__marca
    
    def multVenta(self):
        return self.__multVenta

def asignarDatos(dispositivo, tipoDis, modeloDis, precioDis, almacenamientoDis, ramDis,
                 sistemaOperativoDis, resolucionCamaraDis, conectividadDis):
    dispositivo.tipo = tipoDis
    dispositivo.modelo = modeloDis
    dispositivo.precio = precioDis
    dispositivo.almacenamiento = almacenamientoDis
    dispositivo.ram = ramDis
    dispositivo.sistemaOperativo = sistemaOperativoDis
    dispositivo.resolucionCamara = resolucionCamaraDis
    dispositivo.conectividad = conectividadDis
    dispositivo.precioVenta = precioDis * dispositivo.multVenta()

def obtenerDatos(dispositivo):
    print("***** Registro de Información del Dispositivo *****")
    tipoDis = input("Especifique el tipo de dispositivo (Laptop, Teléfono, Tablet): ")
    modeloDis = input(f"Ingrese el modelo del {tipoDis}: ")
    precioDis = float(input(f"Ingrese el precio del {tipoDis}: $"))
    almacenamientoDis = int(input("Indique la capacidad de almacenamiento en GB: "))
    ramDis = int(input("Especifique la memoria RAM en GB: "))
    sistemaOperativoDis = input("Indique el sistema operativo del dispositivo: ")
    resolucionCamaraDis = input("Especifique la resolución de la cámara en megapíxeles (MP): ")
    conectividadDis = input("Indique las opciones de conectividad (4G, 4.5G, 5G, etc.): ")
    
    asignarDatos(dispositivo, tipoDis, modeloDis, precioDis, almacenamientoDis, ramDis,
                 sistemaOperativoDis, resolucionCamaraDis, conectividadDis)

def mostrarDatos(dispositivo):
    print("********** Detalles del Dispositivo **********")
    print(f"Tipo de Dispositivo: {dispositivo.tipo}")
    print(f"Marca: {dispositivo.marca()}")
    print(f"Modelo: {dispositivo.modelo}")
    print(f"Almacenamiento: {dispositivo.almacenamiento} GB")
    print(f"Memoria RAM: {dispositivo.ram} GB")
    print(f"Sistema Operativo: {dispositivo.sistemaOperativo}")
    print(f"Resolución de la Cámara: {dispositivo.resolucionCamara} MP")
    print(f"Conectividad: {dispositivo.conectividad}")
    print(f"Precio de Venta: ${dispositivo.precioVenta:.2f}")

def main():
    dispositivos_lista = []
    
    while True:
        dispositivo = Dispositivos()
        obtenerDatos(dispositivo)
        dispositivos_lista.append(dispositivo)
        mostrarDatos(dispositivo)
        
        while True:
            continuar = input("¿Desea continuar ingresando dispositivos? (S/N): ").lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Respuesta no válida, por favor ingrese 'S' o 'N'.")
        
        if continuar == 'n':
            break
    
    print("\n********** Dispositivos Registrados **********")
    for dispositivo in dispositivos_lista:
        mostrarDatos(dispositivo)
    
    print("Fin del programa")

main()

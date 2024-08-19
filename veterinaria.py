class Perro:
    Nombre = ""
    Sexo = ""
    Edad = {"Años": 0, "Meses": 0}
    Peso = 0
    Categoría = ""
    Raza = ""
    Discapacidad = True
    Alergias = False
    DescripcionAlergias = ""
    __Tipo = ""
    Estado = "No atendido"
    
    def __init__(self):
        self.__Tipo = "Perro"
        self.Estado = "Registro"
    
    def Tipo(self):
        return self.__Tipo
    
    def EstadoCliente(self):
        self.Estado = "Atendido"
        return self.Estado

def PasarDatos(perro, NombrePerro, EdadAnios, EdadMeses, SexoP,
               RazaPerro, DiscapPerro, PesoPerro, CategoríaPerro, AlergiasPerro, DescripcionAlergias):
    perro.Nombre = NombrePerro
    perro.Edad = {"Años": EdadAnios, "Meses": EdadMeses}
    perro.Sexo = SexoP.lower()
    perro.Peso = PesoPerro
    perro.Categoría = CategoríaPerro
    perro.Raza = RazaPerro
    perro.Discapacidad = DiscapPerro
    perro.Alergias = AlergiasPerro
    perro.DescripcionAlergias = DescripcionAlergias

def ObtenerDatos(perro):
    print("""Ingrese los datos del perro:
─────▄█▄█─────────────
────█████▄▄▄──────────
──────███████▄────────
──────█▀█▀█████───────
─────▄█▄█─▄████▄▄▀────""")
    NombrePerro = input("Nombre de la Mascota: ")
    EdadAnios = int(input("Edad de la Mascota (Años): "))
    EdadMeses = int(input("Edad de la Mascota (Meses): "))
    
    while True:
        SexoP = input("Género de la Mascota (M/F): ").upper()
        if SexoP in ["M", "F"]:
            SexoP = SexoP.lower()
            break
        else:
            print("Error, respuesta no válida, ingrese M o F")

    RazaPerro = input("Raza de la Mascota: ")
    
    while True:
        DiscapPerro = input("¿Posee discapacidad? (sí/no): ").lower()
        if DiscapPerro in ["sí", "si", "no"]:
            Discapacidad = DiscapPerro in ["sí", "si"]
            break
        else:
            print("Error, respuesta no válida, ingrese sí o no")

    PesoPerro = float(input("Ingrese el peso del Perro (kg): "))  
    if PesoPerro >= 10:
        CategoríaPerro = "Perro Grande"
    else:
        CategoríaPerro = "Perro Pequeño"
    
    while True:
        AlergiasPerro = input("¿Tiene alergias? (sí/no): ").lower()
        if AlergiasPerro in ["sí", "si", "no"]:
            Alergias = AlergiasPerro in ["sí", "si"]
            if Alergias:
                DescripcionAlergias = input("Por favor, mencione cuáles son las alergias: ")
            else:
                DescripcionAlergias = ""
            break
        else:
            print("Error, respuesta no válida, ingrese sí o no")

    PasarDatos(perro, NombrePerro, EdadAnios, EdadMeses, SexoP, RazaPerro, Discapacidad, PesoPerro, CategoríaPerro, Alergias, DescripcionAlergias)

def MostrarDatos(perro):
    print("""
........z Z z
(”)_(”)_.-””-.,
 `_ _ `; -._, `)_
( o_, )` __) `-._)___
""")
    print(f"Animal: {perro.Tipo()}")
    print(f"Nombre: {perro.Nombre}")
    print(f"Edad de {perro.Nombre}: {perro.Edad['Años']} años y {perro.Edad['Meses']} meses")
    print(f"Género de {perro.Nombre}: {perro.Sexo}")
    print(f"Raza: {perro.Raza}")
    print(f"Paciente {perro.Nombre}: {'Posee discapacidad' if perro.Discapacidad else 'No posee discapacidad'}")
    print(f"Peso de {perro.Nombre}: {perro.Peso} kg")
    print(f"Categoría: {perro.Categoría}")
    
    if perro.Categoría == "Perro Grande":
        print("""
            ░░░░░░░░░░▐▐░
            ▐░░░░░░░▄██▄▄
            ░▀▀██████▀░░░
            ░░░▐▐░░▐▐░░░░
            ▒▒▒▐▐▒▒▐▐▒▒▒▒""")
    elif perro.Categoría == "Perro Pequeño":
        print("""
            ░▓▓░░░░░
            ░░▓▓▓▓╝░
            ▒▒▓▒▒▓▒▒""")
    
    print(f"Alergias: {'Sí' if perro.Alergias else 'No'}")
    if perro.Alergias:
        print(f"Descripción de alergias: {perro.DescripcionAlergias}")
    print(f"Estado cliente: {perro.EstadoCliente()}")

perro1 = Perro()
perro2 = Perro()

ObtenerDatos(perro1)
ObtenerDatos(perro2)

MostrarDatos(perro1)
MostrarDatos(perro2)

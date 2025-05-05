import random
import names
import re

def crearbaseNamesEs():
    try:
        cantidad = int(input("Digite la cantidad de estudiantes: "))
        porcentaje = int(input("Ingrese qué porcentaje de estos estudiantes desea ingresar a la base de datos: %"))
        annoInicial = int(input("Digite el año inicial de entra de dichos estudiantes: "))
        annoFinal = int(input("Digite el año limite de entrada de dichos estudiantes: "))
        if annoInicial > annoFinal:
            print("El año inicial de entrada debe ser menor o igual a año limite de entrada.")
            return crearbaseNamesEs()
        return valorNotas(cantidad, porcentaje, annoInicial, annoFinal)
    except ValueError:
        print("Por favor ingrese valores validos.")
    
def valorNotas(cantidad, porcentaje, annoInicial, annoFinal):
    try:
        valorNota1 = int(input("Ingrese el valor de la primera nota: "))
        valorNota2 = int(input("Ingrese el valor de la segunda nota: "))
        valorNota3 = int(input("Ingrese el valor de la tercer nota: "))
        if valorNota1+valorNota2+valorNota3!=100:
            print ("Los valores de las notas deben sumar un total de 100.")
    except ValueError:
        print ("")
    return crearbaseNames(cantidad, porcentaje, annoInicial, annoFinal, valorNota1, valorNota2, valorNota3)

def crearbaseNames(cantidad, porcentaje, annoInicial, annoFinal, valorNota1, valorNota2, valorNota3):
    nombres = []
    for i in range(cantidad):
        generoBool = random.choice([True, False])  # Se crea un género como booleano

        nombreCompleto = names.get_full_name(gender=generoBool)  # Se genera el nombre completo
        nombre = nombreCompleto.split()[0]       # Separa el nombre
        apellido1 = nombreCompleto.split()[1]    # Separa el apellido #1

        apellido2 = names.get_last_name()         # Crea el apellido #2 y revisa que no sea igual al otro
        while apellido2 == apellido1:
            apellido2 = names.get_last_name()

        #Carnet
        listaCarnets= []
        with open('sedes.txt', 'r', encoding='utf-8') as archivo:
            sedes = [linea.rstrip('\n') for linea in archivo] #Lo recorre linea por linea

        codigoSede = random.randint(1, len(sedes))  # Genera un código entre 1 y la cantidad de sedes en el archivo
        inicioCarnet = random.randint(annoInicial, annoFinal)
        medioCarnet = f"0{codigoSede}"
        finalCarnet = random.randint(999, 9999)
        carnet = str(inicioCarnet)+str(medioCarnet)+ str(finalCarnet)  #Los une 
        

        while carnet in listaCarnets:
            finalCarnet = random.randint(999, 9999)
            carnet = str(inicioCarnet)+str(medioCarnet)+ str(finalCarnet)
        listaCarnets.append(carnet)


        #Correo
        correosGenerados = []  

        letra_inicial = nombre[0].lower() # Genera el correo
        apellido_correo = apellido1.lower()

        correo = ""
        while True:
            numeros = f"{random.randint(0, 9999):04}"
            correo = str(letra_inicial)+ str(apellido_correo) + str(numeros)+ "@estudiantec.cr" #Crea el correo
            if correo not in correosGenerados:
                correosGenerados.append(correo)
                break  #Lo rompe si el correo no existe 

        # 3 notas random
        nota1 = random.randint(0, 100)
        nota2 = random.randint(0, 100)
        nota3 = random.randint(0, 100)
        promedio = ((nota1 + nota2 + nota3) * 100) / 300
        nota4Provisional = 0.0
        nota5Provisional = 0.0
        notas = ((nota1, nota2, nota3, nota4Provisional, nota5Provisional))

        int(promedio * 10) / 10

        persona = [(nombre, apellido1, apellido2), generoBool, carnet, correo, notas]
        nombres.append(persona)  # Se unen todos

    estudiAMostrar = int((porcentaje / 100) * cantidad)

    muestra = random.sample(nombres, estudiAMostrar)

    for estudiante in muestra:
        print(estudiante) 

    return estudiAMostrar, nombres
crearbaseNamesEs()

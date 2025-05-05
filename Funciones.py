import random
import names
import re

#Entrada y salida con la libreria Names
def crearbaseNamesEs():
    try:
        cantidad = int(input("Digite la cantidad de estudiantes: "))
        porcentaje = int(input("Ingrese qué porcentaje de estos estudiantes desea ingresar a la base de datos: %"))
        annoInicial = int(input("Digite el año inicial de entra de dichos estudiantes: "))
        annoFinal = int(input("Digite el año limite de entrada de dichos estudiantes: "))
        if annoInicial > annoFinal:
            print("El año inicial de entrada debe ser menor o igual a año limite de entrada.")
            return crearbaseNamesEs()
        return crearBaseNames(cantidad, porcentaje, annoInicial, annoFinal)
    except ValueError:
        print("Por favor ingrese valores validos.")
        return crearbaseNamesEs()

#Crea su parte de la base con Names
def crearBaseNames(cantidad, porcentaje, annoInicial, annoFinal):
    cantidadAGenerar = int((porcentaje / 100) * cantidad)
    porcentajesUsuario = porcentajesNotas()
    listaCarnets = []
    listaCorreos = []
    baseDatos = []
    for i in range(cantidadAGenerar):
        nombreYGenero = generarNombre()
        nombre = (nombreYGenero[0], nombreYGenero[1], nombreYGenero[2]) 
        genero = nombreYGenero[3]

        carnet = crearCarnet(annoInicial, annoFinal)
        while carnet in listaCarnets: #revisa que el carnet no esté en la lista
            carnet=crearCarnet(annoInicial, annoFinal)
        listaCarnets.append(carnet)

        correo = generarCorreo(nombre[0], nombre[1]) #Genera el correo sacando el nombre y el apellido de la tupla nombre
        while correo in listaCorreos: #Revis que el correo no esté en la lista
            correo = generarCorreo(nombre[0], nombre[1])
        listaCorreos.append(correo)

        notas = notasRandom(porcentajesUsuario[0], porcentajesUsuario[1], porcentajesUsuario[2]) #Saca los porcentajes de la tupla porcentajesUsuario
        baseDatos.append([nombre, genero, carnet, correo, notas])
    print ("[")
    for estudiante in baseDatos:
        print (estudiante)
    print ("]")

#Nombre
def generarNombre():
    genero = random.choice(['male', 'female'])  # Se crea un género 
    nombreCompleto = names.get_full_name(genero)  # Se genera el nombre completo
    nombre = nombreCompleto.split()[0]       # Separa el nombre
    apellido1 = nombreCompleto.split()[1]    # Separa el apellido #1

    apellido2 = names.get_last_name()         # Crea el apellido #2 y revisa que no sea igual al otro
    while apellido2 == apellido1:
        apellido2 = names.get_last_name()
    
    genero = True if genero == 'male' else False

    return nombre, apellido1, apellido2, genero

#Carnet
def crearCarnet(annoInicial, annoFinal):
    sedes = []
    with open('sedes.txt', 'r') as archivo:
        for linea in archivo:
            sedes.append(linea.rstrip('\n'))

    codigoSede = random.randint(1, len(sedes))  # Genera un código entre 1 y la cantidad de sedes en el archivo
    inicioCarnet = random.randint(annoInicial, annoFinal)
    if len(sedes)<10:
        codigoSede = "0"+str(codigoSede)
    else:
        codigoSede = str(codigoSede)
    finalCarnet = random.randint(1000, 9999)
    carnet = int(str(inicioCarnet)+str(codigoSede)+ str(finalCarnet))  #Los une 
    return carnet

#Correo
def generarCorreo(nombre, apellido1):

    letraInicial = nombre[0].lower() # Genera el correo
    apellidoCorreo = apellido1.lower()
   
    numeros = random.randint(1000, 9999)
    correo = letraInicial+ apellidoCorreo + str(numeros)+ "@estudiantec.cr" #Crea el correo
    return correo

#Cuanto vale cada nota
def porcentajesNotas():
    try:
        porcentaje1 = int(input("Ingrese el valor de la primera nota: "))
        porcentaje2 = int(input("Ingrese el valor de la segunda nota: "))
        porcentaje3 = int(input("Ingrese el valor de la tercer nota: "))
        if porcentaje1 + porcentaje2 + porcentaje3 != 100:
            print ("Los valores de las notas deben sumar un total de 100.")
            return porcentajesNotas()
        return porcentaje1, porcentaje2,  porcentaje3
    except ValueError:
        print ("Solo se admiten valores numericos enteros. ")
        return porcentajesNotas()

#Notas aleatorias
def notasRandom(porcentaje1, porcentaje2, porcentaje3):
    nota1 = random.randint(0, 100)
    nota2 = random.randint(0, 100)
    nota3 = random.randint(0, 100)
    nota1Real = nota1 * (porcentaje1/100)
    nota2Real = nota2 * (porcentaje2/100)
    nota3Real = nota3 * (porcentaje3/100)
    promedio = (nota1Real + nota2Real + nota3Real)
    nota4 = promedio
    nota5 = promedio
    notas = ((nota1, nota2, nota3, nota4, nota5))
    return notas

#def ordenarPorGenero(listatotal):


def borrar(cantidad, porcentaje, annoInicial, annoFinal, valorNota1, valorNota2, valorNota3):
    estudiantes = []
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
        estudiantes.append(persona)  # Se unen todos

    estudiAMostrar = int((porcentaje / 100) * cantidad)

    muestra = random.sample(estudiantes, estudiAMostrar)

    for estudiante in muestra:
        print(estudiante) 

    return estudiAMostrar, estudiantes

#print(generarNombre())
#print(crearCarnet(2022,2025))
#print(generarCorreo("Marciano", "Cantero"))
#porcentajesNotas()
#crearbaseNamesEs()
#crearBaseTXT(37)


import random
import names
import pickle
import re
import smtplib

#Entrada y salida con el documento
# def crearBaseTXTEs():
#     """
#     Entradas: 
#     """
#     try:
#         porcentaje = int(input("Ingrese qué porcentaje de estos estudiantes desea ingresar a la base de datos: %"))
#         annoInicial = int(input("Digite el año inicial de entra de dichos estudiantes: "))
#         annoFinal = int(input("Digite el año limite de entrada de dichos estudiantes: "))
#         if annoInicial > annoFinal:
#             print("El año inicial de entrada debe ser menor o igual a año limite de entrada.")
#             return crearBaseTXT(porcentaje, annoInicial, annoFinal)
#         return crearBaseTXT(porcentaje, annoInicial, annoFinal)
#     except ValueError:
#         print("Por favor ingrese valores validos.")
#         return crearBaseTXT()

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
    """
    Genera un carnet de estudiante con el formato Año/Sede/Numero aleatorio, validado con una expresión regular.

    - AAAA: Año de ingreso aleatorio entre annoInicial y annoFinal.
    - SS: Código de sede de 2 dígitos (01, 02, ..., 10, ...).
    - NNNN: Número aleatorio de 4 dígitos.

    Devuelve:
    - carnet (int): Número de carnet si cumple el formato esperado.
    """
    patron =  r"^[123456789+$]"
    sedes = []
    with open('sedes.txt', 'r') as archivo:
        for linea in archivo:
            sedes.append(linea.rstrip('\n')) #Lee linea por linea y lo añade a la lista vacia

    codigoSede = random.randint(1, len(sedes))  # Genera un código entre 1 y la cantidad de sedes en el archivo
    inicioCarnet = random.randint(annoInicial, annoFinal)
    if len(sedes)<10:
        codigoSede = "0"+str(codigoSede)
    else:
        codigoSede = str(codigoSede)
    finalCarnet = random.randint(1000, 9999)
    carnet = int(str(inicioCarnet)+str(codigoSede)+ str(finalCarnet))  #Los une 
    if not re.fullmatch(patron, carnet):
        return carnet
    else:
        return crearCarnet(annoInicial, annoFinal)

#Correo
def generarCorreo(nombre, apellido1):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+$" #Solo acepta letras y caracteres especiales

    if not re.fullmatch(patron, nombre) or not re.fullmatch(patron, apellido1): #Revisa que el nombre y apellido tengan el patron esperado
        raise ValueError("El nombre y el primer apellido deben contener solo letras sin espacios ni caracteres especiales.")

    inicial = nombre[0].lower()
    apellidoAUsar = apellido1.lower()
    numeros = str(random.randint(1000, 9999))

    correo = f"{inicial}{apellidoAUsar}{numeros}@estudiantec.cr" #Genera el correo
    return correo

#Cuanto vale cada nota
def porcentajesNotas():
    try:
        porcentaje1 = int(input("Ingrese el valor de la primera nota: "))
        porcentaje2 = int(input("Ingrese el valor de la segunda nota: "))
        porcentaje3 = int(input("Ingrese el valor de la tercer nota: ")) #Pide cuanto vale cada nota para la nota fianl
        if porcentaje1 + porcentaje2 + porcentaje3 != 100:
            print ("Los valores de las notas deben sumar un total de 100.")
            return porcentajesNotas()
        return porcentaje1, porcentaje2,  porcentaje3 #Los retorna como tupla para usarlos más tarde
    except ValueError:
        print ("Solo se admiten valores numericos enteros. ")
        return porcentajesNotas() #En caso de dar error vuelve a la función y no corta el programa

#Notas aleatorias
def notasRandom(porcentaje1, porcentaje2, porcentaje3):
    nota1 = random.randint(0, 100)
    nota2 = random.randint(0, 100)
    nota3 = random.randint(0, 100)
    nota1Real = nota1 * (porcentaje1/100)
    nota2Real = nota2 * (porcentaje2/100)
    nota3Real = nota3 * (porcentaje3/100)
    promedio = (nota1Real + nota2Real + nota3Real)
    nota4 = int(promedio)
    nota5 = int(promedio)
    notas = ((nota1, nota2, nota3, nota4, nota5))
    return notas

def crearBaseEs():
    baseLista = []
    try:
        cantidad = int(input("Digite la cantidad de estudiantes: "))
        porcentaje = int(input("Ingrese qué porcentaje de estos estudiantes desea ingresar a la base de datos: %"))
        annoInicial = int(input("Digite el año inicial de entra de dichos estudiantes: "))
        annoFinal = int(input("Digite el año limite de entrada de dichos estudiantes: ")) 
        porcentajesAUsar = porcentajesNotas() #Pide los inputs de todo
        if annoInicial > annoFinal:
            print("El año inicial de entrada debe ser menor o igual a año limite de entrada.")
            return crearBaseEs()
        if porcentaje > 100 or porcentaje < 0:
            print("El porcentaje ingresado no es válido.")
            return crearBaseEs()
        if cantidad < 0:
            print("El numero de estudiantes ingresado es invalido.")
            return crearBaseNames()
        tuplaNames = crearBaseNames(cantidad, porcentaje, annoInicial, annoFinal, porcentajesAUsar)
        listaNames = tuplaNames[0]
        carnetsNames = tuplaNames[1]
        correosNames = tuplaNames[2]
        listaTXT = crearBaseTXT(carnetsNames, correosNames, annoInicial, annoFinal, porcentajesAUsar)
        baseFinal = listaNames + listaTXT
        baseLista.append(baseFinal)
        print ("[")
        for estudiante in baseFinal:
            print(estudiante)
        print ("]")
        return baseFinal
    except ValueError:
        print("Por favor ingrese valores validos.")
        return crearBaseEs() #Si algo esta mal ingresado llama de nuevo a la funcion

#Crea su parte de la base con Names
def crearBaseNames(cantidad, porcentaje, annoInicial, annoFinal, porcentajesAUsar):
    cantidadAGenerar = int((porcentaje / 100) * cantidad)
    listaCarnets = []
    listaCorreos = [] 
    baseDatos = [] #Establezco las 3 listas necesarias
    for i in range(cantidadAGenerar): #Ejecuta el codigo la cantidad de veces que pueda con range(cantidadAGenerar)
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

        notas = notasRandom(porcentajesAUsar[0], porcentajesAUsar[1], porcentajesAUsar[2]) #Saca los porcentajes de la tupla porcentajesAUsar
        baseDatos.append([nombre, genero, carnet, correo, notas])
    return baseDatos, listaCarnets, listaCorreos #Devuelve una tupla por las comas

#Crea su parte de la base
def generarListaTXT():
    with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
        cantidadLineas = 0
        listaTXT = []
        for linea in archivo:
            cantidadLineas += 1
            linea = linea.strip()  # Elimina espacios en blanco al inicio y final, incluyendo el salto de línea
            datos = linea.split(",")  # Convierte la línea en una lista (nombre, apellido1, apellido2, género)
            listaTXT.append(datos)
            
        cantidadImportada = random.randint(0 , cantidadLineas)
        nuevaLista = listaTXT[0:cantidadImportada]
        print("La cantidad aleatoria de estudiantes importados del documento es de " + str(cantidadImportada) + ".")
        return nuevaLista

def crearBaseTXT(carnetsExistentes, correosExistentes, annoInicial, annoFinal, porcentajesAUsar):
    listaEstudiantesTXT = generarListaTXT()
    baseTXT = []
    for estudiante in listaEstudiantesTXT:
        nombre = estudiante[0]
        apellido1 = estudiante[1]
        apellido2 = estudiante[2]
        genero = estudiante[3]
        nombreTupla = (nombre, apellido1, apellido2)
        genero = True if genero == 'Masculino' else False
        correo = generarCorreo(nombre, apellido1)
        while correo in correosExistentes: #correosExistentes viene de crearBaseEs, si la llamara aqui crearia una nueva base
            correo = generarCorreo(nombre, apellido1)
        correosExistentes.append(correo)
        carnet = crearCarnet(annoInicial, annoFinal)
        while carnet in carnetsExistentes: #carnetsExistentes viene de crearBaseEs, si la llamara aqui crearia una nueva base
            carnet = crearCarnet(annoInicial, annoFinal)
        carnetsExistentes.append(carnet)
        notas = notasRandom(porcentajesAUsar[0], porcentajesAUsar[1], porcentajesAUsar[2]) #Es tupla entonces tengo que separarlos con el valor del indice
        estudiante = [nombreTupla, genero, carnet, correo, notas]
        baseTXT.append(estudiante)
    return baseTXT

def generarEstudianteManualES():
    nombreInput = str(input("Escriba el nombre completo del estudiante por favor: "))
    generoInput = int(input("Ahora ingrese 1 o 2 para establecer el genero del estudiante. 1 para masculino, 2 para femenino. Digite: "))
    annoInput = int(input("Ingrese el año de entrada del estudiante"))
    # sedeInput = str(input("¿En qué sede se encuentra este estudiante? 1. Cartago \n"
    # "2. San Carlos\n"
    # "3. San Jose\n"
    # "4. Alajuela"))
    partesNombre = nombreInput.strip().split()
    nombreManual = partesNombre[0]
    apellido1Manual = partesNombre[1]
    apellido2Manual = partesNombre[2]
    print(nombreManual, apellido1Manual, apellido2Manual, generoInput)
    return generarEstudiandoManualAux(nombreManual, apellido1Manual, apellido2Manual, generoInput, annoInput)

def generarEstudiandoManualAux(nombreManual, apellido1Manual, apellido2Manual, generoInput, partesNombre, annoInput):
    if generoInput != 1 or 2:
        print("El valor ingresado es invalido. Digite de nuevo.")
        return generarEstudianteManualES()
    if len(partesNombre) != 3:
        print("El formato del nombre es erroneo. Debe tener 3 palabras, un nombre y dos apellidos. Digite el nombre de nuevo.")
        return generarEstudianteManualES()
    if len(annoInput) != 4 or annoInput != int:
        print("El año ingresado es invalido, digitelo de nuevo.")
        return generarEstudianteManualES()
    return generarEstudianteManual(nombreManual, apellido1Manual, apellido2Manual, generoInput, annoInput)

def generarEstudianteManual(nombreManual, apellido1Manual, apellido2Manual, generoInput, annoInput, porcentaje1, porcentaje2, porcentaje3, baseFinal): #Probar si llamandola en crearBaseES se une bien
    #nuevoEstudiante= []
    nombreTupla = (nombreManual, apellido1Manual, apellido2Manual)
    generoCreado = True if generoInput == 1 else False
    correoManual = generarCorreo(nombreManual, apellido1Manual)
    carnet = crearCarnet(annoInput, annoInput)
    notas = notasRandom(porcentaje1, porcentaje2, porcentaje3)
    estuadianteManual= [nombreTupla, generoCreado, correoManual, carnet, notas]
    #nuevoEstudiante.append(estuadianteManual)
    baseFinal.append(estuadianteManual)
    print(baseFinal)
    
    



#def enviarCorreo()

#def sortearPorNota

#def ordenarPorGenero(baseFinal):     


#generarEstudianteManualES()
#generarListaTXT()
#crearBaseTXT()
#print(generarNombre())
#print(crearCarnet(2022,2025))
#print(generarCorreo("Marciano", "Cantero"))
#print(porcentajesNotas())
#crearBaseEs()
# crearBaseTXT([],[],2022,2025,(40,40,20))
generarEstudianteManual("Pepe", "Marciano","Espinoza", 1, 2022, 35, 35, 30, [])


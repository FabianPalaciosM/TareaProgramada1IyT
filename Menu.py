import Funciones
def menu():
    BDCreada=False
    while True:
        print("1. Crear BD dinamica\n"
        "2. Registrar un estudiante\n"
        "3. Generar reporte HTML y .csv\n"
        "4. Respaldar en XML\n"
        "5. Reporte por género (.docx)\n"
        "6. Gestionar curva\n"
        "7. Envio de correo para reposición\n"
        "8. Aplazados en al menos 2 exámenes (.pdf)\n"
        "9. Estadística por generación\n"
        "10. Reporte por generación\n"
        "11. Salir")

        menu = input("Seleccione la opción que desea: ")

        if menu == "1":
            if BDCreada==True:
                print ("Ya existe la base de datos.")
            else:
                BDCreada=True
        elif menu=="2":
            if BDCreada==False:
                print("La base de datos no está creada")
            elif BDCreada== True:
                print("Ya está creada")
        elif menu == "11":
            print("Gracias por usar el programa") 
            break
        else:
            print("Introduzca un valor válido.")


menu()
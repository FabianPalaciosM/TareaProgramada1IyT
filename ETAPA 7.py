def enviarCorreos(archivoFinal):
    """
    Funcionamiento: Genera un correo automatico para los estudiantes en estado de reposición.
    Entradas:
    archivoFinal(list): Base de datos.
    Salidas:
    Correo: Un correo en bandeja de entrada.

    """
    mensajeBase = (
        "Para: {correo}\n"
        "Asunto: Reposición de evaluación\n"
        "Estimado(a) {nombre}:\n"
        "Su nota final no cumple con los requisitos, por lo que se encuentra en condición de Reposición.\n"
        "Se le estará comunicando sobre la fecha y hora del examen.\n"
        "Atentamente:\n"
        "Escuela de Ingeniería en Computación, Cartago.\n"
    )

    with open("correoBandeja.txt", "w", encoding="utf-8") as salida:
        for estudiante in archivoFinal:
            nombreCompleto, genero, carnet, correo, notas = estudiante
            nota_final = notas[5]
            if nota_final < 67.5:
                mensaje = mensajeBase.format(nombreCompleto, correo)
                salida.write(mensaje)

    print("Correos de Reposición guardados en la bandeja de salida.")

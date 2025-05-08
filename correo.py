def enviarCorreo():
    with open("bandeja_salida.txt", "w", encoding="utf-8") as bandeja:
        for estudiante in baseDatos:
            nombre, genero, carnet, correo, notas = estudiante
            nota_final = notas[4]
            if 50 <= nota_final < 70:
                mensaje = f"""Para: {correo}
Asunto: Reposición de evaluación

Estimado(a) {nombre[0]} {nombre[1]} {nombre[2]},
Su nota final es {nota_final:.2f}, lo que indica que está en condición de Reposición.
Debe presentarse el día {dia} a la hora {hora} para realizar su evaluación de reposición.

Atentamente,
Coordinación Académica

--------------------------------------------------
"""
                bandeja.write(mensaje)
    print("Correos de Reposición guardados en 'bandeja_salida.txt'."
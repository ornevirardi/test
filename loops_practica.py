part_max = int(input ("Por favor ingrese la cantidad de participantes -> "))
print ("")
print ("El sistema ha sido configurado para aceptar",part_max, "participantes")
print("")

cant_part = 0

while (cant_part < part_max):
    nombre = input ("Ingrese su nombre ->")
    print("")
    email = input ("ingrese su email ->")
    print("")
    print (" Hola", nombre, "su email es", email, "desea confirmar la inscripcion?")
    print ("")
    print ("Para confirmar,escriba \"SI\" o escriba \"NO\" para rechazar")
    respuesta = input ()
    respuesta = respuesta.lower()
    if respuesta == "si":
        print("")
        print("********************")
        print ("Gracias, confirmamos su inscripcion, lo esperamos!")
        print("********************")
        print("\n\n\n")
        print("SU NUMERO DE PARTICIPANTE ES", cant_part + 1)
        cant_part += 1
    else:
        print("")
        print("********************")
        print ("operacion cancelada")
        print("********************")
print ("Cantidad maxima alcanzada")


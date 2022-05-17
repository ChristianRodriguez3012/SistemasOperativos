from sympy.crypto.crypto import encipher_shift, decipher_shift

#mensaje=open("C:/Users/nuez_/OneDrive/Escritorio/USALLE/2022-I/SO/PARCIAL/CODIGOS/INVESTIGACION/info.txt","r")
seleccion=str(input("que desea hacer: cifrado(c) - descifrar (d): "))
if seleccion == "c":
    mensaje=str(input("escribir palabra: "))
    cifrado=encipher_shift(mensaje,1)
    print("Mensaje Encriptado: ",cifrado)

if seleccion == "d":
    mensaje=open("C:/Users/nuez_/OneDrive/Escritorio/USALLE/2022-I/SO/PARCIAL/CODIGOS/INVESTIGACION/cifrado.txt","r")
    descifrar=encipher_shift(mensaje, -1)
    print("Mensaje Original: ",descifrar, " ")



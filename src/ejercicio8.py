def cifrar_en_cesar(mensaje, desplazamiento):
    cifrado = ""

    for caracter in mensaje:
        if caracter.isupper():
            cifrado += chr((ord(caracter) - ord('A') + desplazamiento) % 26 + ord('A'))
        elif caracter.islower():
            cifrado += chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            cifrado += caracter
            
    return cifrado

def descifrar_en_cesar(mensaje_cifrado, desplazamiento):
    return cifrar_en_cesar(mensaje_cifrado, -desplazamiento)

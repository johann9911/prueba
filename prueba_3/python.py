def mayor(cadena):
    aux = ""
    for i in range(len(cadena)-1,-1, -1):
        aux += cadena[i]
    return aux

def main():
    cadena = "hello world"
    print(mayor(cadena))

main()
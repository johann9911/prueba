def mayor(arr):
    mayor = -1
    for i in range(len(arr)):
        if arr[i]>mayor:
            mayor=arr[i]
    return mayor

def main():
    arreglo = [2,3,15,6,7]
    print(mayor(arreglo))

main()
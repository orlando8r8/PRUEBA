n = int(input().strip())
a = [] #declaracion matriz a
for a_i in range(n): #se establece el recorrido dependiendo del valor ingresado en n
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]  # se ingresan los valores de la matriz separados por espacios
    a.append(a_t) #se le pega el valor de a_t a la matriz A

def diferencia_diagonal(a): #se declara la funcion diferencia diagonal
    (diagonal_sum1, diagonal_sum2) = (0,0)
    for i in range(len(a)):
        diagonal_sum1 += a[i][i] #se guarda el valor de la suma de la diagonal 1
        diagonal_sum2 += a[i][n-1-i] # se guarda el valor de la suma de la diagonal 2
    return abs(diagonal_sum1 - diagonal_sum2) # retorna el valor absoluto de la diferencia entre las diagonales

print(diferencia_diagonal(a)) #se imprime el resultado de la diferencia diagonal

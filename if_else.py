n = int(input("Escriba un numero entero: ").strip()) #valor de entrada y se eliminan los espacios en blanco iniciales y finales de la cadena.

if n%2!=0: #se divide el valor de entrada y si el cociente es diferente de cero se imprime el mensaje, si no, se procede a la siguiente condicion
    print ("Weird")
    
else:
    if n%2==0 and n>=2 and n<=5: #se valida si el valor de entrada esta en el rango de 2 a 5 y se imprime el mensaje,si no,se procede a la siguiente condicion
        print ("Not Weird")
    
    elif n%2==0 and n>=6 and n<=20: #se valida si el valor de entrada esta en el rango de 6 a 20 y se imprime el mensaje,si no,se procede a la siguiente condicion
        print ("Weird")
    elif n%2==0 and n>20: #si el valor es mayor a 20 se imprime el mensaje finalizando la ultima condicion del programa
        print ("Not Weird")

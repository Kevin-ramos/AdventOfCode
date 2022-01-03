
#para procesar la entrada de los binarios
with open('dia4.txt') as fin:
    #separo los numeros de las tablas
    numerosBingo, *boards= fin.read().split('\n\n')
    #el problema que estan como string y las necesito como una lista
    #separo cada elemento a entero   
    numerosBingo=[int(i) for i in numerosBingo.split(',')]
    conjuntoTablas=[[[int(columna) for columna in fila.split()] for fila in tabla.split('\n')] for tabla in boards]    
 ##ubicar una x sin un numbero coincide
def marcarNumero(number,board):
    for fila in board:
        #por cada fila
        for columna in range(0, len(fila)):
            # voy cambiando de columna y comparo si es que existe ese numero
            if fila[columna] == number:
                #si existe ese numero maroc con una x
                fila[columna]='x'
# suma odos los numeros no marcados con x
def sumaNoMarcado(board):
    sum = 0
    for fila in board:
        for num in fila:
            #para cada numero en la fila 
            #si es diferente de x
            if num !='x':
                #sigo sumando el numero corrrespondiente
                sum+=num
    return sum
    #verificar si hay un ganador
def verificarGanador(tabla):
    existeTablaGanadora=False
    for fila in tabla:
        #si es que una fila se encuentra con todos los elementos de x es la ganadora y lo mismo con la columna
        existeTablaGanadora=all(elem in ['x'] for elem in fila)
        if existeTablaGanadora:
            return existeTablaGanadora
        #check columns
    for col in range(0,5):
        existeTablaGanadora= all(elem in ['x'] for elem in [row[col] for row in tabla])
        if existeTablaGanadora:
            return existeTablaGanadora
    return existeTablaGanadora

    #part1
def solucion():
    todasTablas=conjuntoTablas
    for numero in numerosBingo:
        for tabla in todasTablas:
            marcarNumero(numero,tabla)
            if verificarGanador(tabla):
           
                return sumaNoMarcado(tabla)*numero
#part 2 dejar ganar al calamar






def part2():
    tablasTodas=conjuntoTablas
    numeros= numerosBingo

    ganadorEncontrado=False
    while not ganadorEncontrado:
        number=numeros[0]
        numeros= numeros[1:]

        for board in tablasTodas:
            marcarNumero(number, board)
        index=0
        while index< len(tablasTodas):
            if verificarGanador(tablasTodas[index]):
                if len(tablasTodas) >1:
                    tablasTodas.pop(index)
                else:
                    ganadorEncontrado= True
                    return sumaNoMarcado(tablasTodas[index])* number
                
            else:
                index +=1
print('parte2', part2())

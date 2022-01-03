
#para procesar la entrada de los binarios
with open('dia3.txt') as finArchivo:

    datos= [i for i in finArchivo.read().strip().split('\n')]
    dato=finArchivo.read().split('\n')
    print(dato)

"""

def binarioAEntero(stringBinario):
    return int(stringBinario,2)

#encintrabdi el consumo de energia
def consumoEnergia():
    #el mas comun enterio de cada fila
    gammaRate=[]
    epsilonRate=[]
    #bucle desde 0 hasta el tamaño - 1 de los binarios
    for column in range(0, len(datos[0])):
        #inicializacion de banderas
        cero=0
        uno=0
        #cada uno de los datos en el la lista se iguala al bitstring
        for bitString in datos:
            if bitString[column]=='0':
                cero+=1
            else:
                uno+=1
        if cero>uno:
            gammaRate.append('0')
            epsilonRate.append('1')
        elif uno>cero:
            gammaRate.append('1')
            epsilonRate.append('0')
    #transformacion de binarios a decimales
    #como el gammarate, es una lista con cada uno de los elementos, quiero transformar a string

    
    #metodo para transformar a string ''.join
    gammaRate=''.join(gammaRate)

    epsilonRate=''.join(epsilonRate)
   
    consumoDeEnergia= binarioAEntero(gammaRate)* binarioAEntero(epsilonRate)
    return consumoDeEnergia

##parte 2 tasa de soporte vital
def tasaSoporte():
    primerDato= datos.copy()
    #tasa de oxigeno
    i=0
    while len(primerDato) > 1:
        cero= 0
        uno= 0
         #contador
        for bitString in primerDato:
            if bitString[i]=='0':
                cero+=1
            else:
                uno+=1
        #escuchar el mas corto
        if cero>uno:
            primerDato= [bitString for bitString in primerDato if bitString[i] =='0']
        else:
            primerDato= [bitString for bitString in primerDato if bitString[i] =='1']
           
        i+=1
    oxigenoRate=''.join(primerDato)

    segundoDato=datos.copy()
    i=0
    while len(segundoDato) > 1:
        cero=0
        uno=0
         #contador
        for bitString in segundoDato:
            if bitString[i]=='0':
                cero+=1
            else:
                uno+=1
        #escuchar el mas corto
        if cero>uno:
            segundoDato= [bitString for bitString in segundoDato if bitString[i]=='1']
        else:
            segundoDato= [bitString for bitString in segundoDato if bitString[i]=='0']
        i+=1
        co2Rate=''.join(segundoDato)
    return binarioAEntero(oxigenoRate)* binarioAEntero(co2Rate)
print(tasaSoporte())

##print(consumoEnergia())
"""


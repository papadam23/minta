import random


def elso():
    lista=[]
    for i in range(5):
       szam=[int (input("Kérek egy egész számot!"))]
       lista.append(szam)
    return lista

def masodik():
    logikai=[]
    for i in range(7):
        if random.randint(1,2)==1:
            logikai.append(True)
        else:
            logikai.append(False)
    return logikai

def harmadik():
    lista=[]
    for i in range(10):
       szam= random.randint(5,25)
       lista.append(szam)
    print(lista)
    #print(lista[::-1])
    #lista.reverse() ez is megfordítja
    #print(lista)
    print(lista[0::2])
    szam=   int (input("Kérek egy egész számot! 1-10 között"))


def negyedik():
    lista=[1.2,5.3,6.1]
    lista2=[0.2,4.2,5.6]
    lista3=[lista+lista2]
    print(*lista3)

def otodik():
    lista=[1,2,3,4,5,6,7]
    lista2=[1,2,3,4,5,6,7]
    lista.pop(6)
    lista.insert(0,7)
    print(lista)
    lista2.pop(0)
    lista2.insert(6,1)
    print(lista2)

def hatodik():
    szam=   int (input("Kérek egy egész számot!"))
    lista=[]
    for i in range(szam):
        lista.append(szam)
        szam+=1
    lista.reverse()

    print(lista)

def hetedik():
    szam=   int (input("Kérek egy egész számot!"))
    lista=[]
    valos=1
    ker=1
    for i in range(szam):
        lista.append(valos)
        valos+=0.5
        lista=[ker+valos]
        valos==ker
        
    print(lista)
    
    

    




def main():
    #print(elso())
    #print(masodik())
    #harmadik()
    #negyedik()
    #otodik()
    #hatodik()
    hetedik()

main()
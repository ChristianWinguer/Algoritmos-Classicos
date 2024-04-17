
# Função recursiva com LOOP INFINITO!
def regressivaLoopInfinito(i):
    print (i)
    regressiva(i - 1)

#print ('minha função recursiva com LOOP INFINITO')
#print (regressivaLoopInfinito(3))

def regressiva(i):
    print (i)

    #Caso-base
    if i <= 1:
        return
    
    #Caso recursivo
    else:
        regressiva(i-1)

print("Minha função regressiva")
print(regressiva(3))

def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

x = 3
print(f"O fatorial de {x} é {fatorial(x)}")
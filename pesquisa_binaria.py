
# Função de pesquisa binária | Recebe uma lista e um objetivo dentro da lista
def pesquisa_binaria (lista, item) :

    #Acompanhamento da parte da lista que você está procurando
    nBaixo = 0
    nAlto = len(lista) - 1

    while nBaixo <= nAlto:

        #verifica o elemento central da lista
        nMeio = (nBaixo + nAlto) // 2
        chute = lista[nMeio]

        #Achou o item desejado
        if chute == item:
            return nMeio
        
        #Chutou alto demais
        if chute > item:
            nAlto = nMeio - 1

        #Chutou baixo demais
        else:
            nBaixo = nMeio + 1

    #O item não existe
    return None

#criando minha lista
minhaLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print ("MEUS RESULTADOS:")
print (pesquisa_binaria(minhaLista, 6)) # Saída: 4 (índice de 5 na lista)
print (pesquisa_binaria(minhaLista, -1)) # Saída: None (pois -1 não está na lista)

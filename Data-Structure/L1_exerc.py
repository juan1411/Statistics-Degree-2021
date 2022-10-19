from copy import deepcopy


# funções: ------------------------------------------------------------------------------------------------- #

def testeRainhaV3(tab, n, coordY=0):
    # testa TODAS as combinações
    # tab: um tabuleiro (matriz n por n)
    # n: as dimensões
    # comb: existência ou não de combinações válidas
    # coordY: coordenada da linha para iterar 

    global existeCombinacao
    # isso é um truque para os prints saírem corretos
            
    for coordX in range(n):
    # valores de [0, n-1] que percorrem as colunas, fixado uma linha (coordY)

        if tab[ coordY ][ coordX ] == "pode":
        # se for possível colocar uma peça, coloque-a e atualize o tabuleiro

            new_tab = update(deepcopy(tab), coordY, coordX)
            # inclusive, não sabia se podia usar módulos, mas realmente não estava conseguindo
            # fazer o meu código funcionar sem o "deepcopy" para as matrizes ...
            # fiquei sem memória durante alguns testes, mas "funciona"

            #se estiver na última linha, retorne o novo tabuleiro e de continuidade aos "for"s anteriores
            if coordY == (n-1): 
                printMatriz(new_tab)
                existeCombinacao = True # isso é um truque para os prints saírem corretos
                return

            else: testeRainhaV3(new_tab, n, coordY+1)
            # do contrário, rechame a função e, dessa forma, será feito a mesma coisa de verificar 
            # posições livres até a última linha.
            # como é quase um "for encaixado", a função testa todas as combinações de peças em diferentes colunas

    return
    # se o algoritmo chegar até aqui, é porque alguma linha ficou sem espaços livres,
    # então retorne e de continuidade aos "for"s anteriores


def update(tab, linha, coluna):
    # coloca a peça e restringue as opções
    # tab: um tabuleiro (matriz n por n)
    # linha, coluna: onde será colocado a peça

    #excluindo a linha e a coluna
    for lc in range(len(tab)):

        tab[linha][lc] = "0" #zera a linha
        tab[lc][coluna] = "0" #zera a coluna

    #excluindo a diagonal (anterior): Já foi zerada
    #excluindo a diagonal (posterior):
    for i in range(1, len(tab)+1):
        try:
            if (coluna+i) < len(tab):
                tab[linha+i][coluna+i] = "0" # a direita 
                
            if (coluna-i) >= 0:
                tab[linha+i][coluna-i] = "0" # a esquerda
                
        except IndexError: pass

    tab[linha][coluna] = "1" # coloca a peça
    return tab


def printMatriz(matriz):
    # função para ajeitar os prints (o run.codes é chato com isso)
    # matriz: um 'tabuleiro válido'

    global existeCombinacao

    if existeCombinacao: print()
    # se já existe uma combinação, então é preciso separá-las (\n)

    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
                    
        print() # quebra de linha


# ---------------------------------------------------------------------------------------------------------- #

# Programa principal

def main():
    # facilita os meus testes

    #Entrada:
    N = int(input())

    # n é natural ?
    if N <= 0:
        print("sem solucao")

    else:
        tabuleiro = [ ["pode" for j in range(N)] for u in range(N)]
        # python .... isso ai cria uma matriz n por n, com "pode" dentro ...

        global existeCombinacao
        existeCombinacao = False
        # a função "testeRainhaV3" altera a variável caso exista pelo menos uma combinação válida

        testeRainhaV3(tabuleiro, N, existeCombinacao)

        if not existeCombinacao: print("sem solucao")


main()

# testes:

'''print("N = 1")
main(1)

print("N = 2")
main(2)

print("\nN = 3")
main(3)

print("\nN = 4")
main(4)

print("\nN = 5")
main(5)

print("\nN = 6")
main(6)

print("\nN = 8")
main(8)'''

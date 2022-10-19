"""
Lista 9
Componentes do grupo :
NUSP : 11912787

  Programa que constroi uma arvore binaria a partir de uma entrada de dado, cuja forma
eh bem especifica: abre parenteses, o nome de um conjunto, uma operacao, o nome do outro
conjunto e fecha parenteses. E depois calcula o conjunto resultante de todas a operacoes.
  Para isso, defini um TAD para arvores binarias e outro para os conjuntos; cada um possui
apenas os metodos necessarios para que o programa funcione.
  Tambem foi preciso criar tres funcoes auxiliares: uma para tratar da construcao da arvore
a partir de uma frase passada, outra para colocar os valores dos conjuntos dentro da arvore
e, por fim, uma para calcular o resultado das operacoes (e para esta funcionar corretamente,
foi necessario o uso de um TAD pilha, uma lista encadeada).
"""

class Celula:
    """ Define a classe Celula, que armazena um elemento da pilha.
    :atrib valor: que esta armazenado
    :atrib prox: indica qual o proximo elemento da pilha
    """
    def __init__(self, valor):
        """ Metodo construtor.
        :param valor: que sera armazenado
        """
        self.valor = valor
        self.prox = None


class Pilha:
    """ Define a classe a Pilha, que representa o TAD pilha, usando uma lista encadeada.
    :atrib tam: tamanho da pilha
    :atrib topo: ultimo elemento adicionado
    """
    def __init__(self):
        """ Metodo construtor."""
        self.tam = 0
        self.topo = None

    def __str__(self):
        """ Metodo para definir o print do objeto.
        :return: a string de como eh o print
        """
        atual = self.topo
        saida = ""
        while (atual):
            saida += str(atual.valor) + "->"
            atual = atual.prox
        return saida

    def estaVazia(self):
        """ Metodo que indica se a pilha esta vazia ou nao.
        :return: True, se estiver vazia; False, caso contrario
        """
        if (self.tam == 0):
            return True
        return False

    def empilha(self, valor):
        """ Metodo para inserir um novo elemento no topo da pilha.
        :param valor: valor que sera armazenado
        """
        novo = Celula(valor)
        novo.prox = self.topo
        self.topo = novo
        self.tam += 1

    def desempilha(self):
        """ Metodo para retirar o elemento no topo da pilha.
        :return: o valor do elemento no topo
        :exception: "PilhaVazia", se a pilha estiver vazia
        """
        if (self.estaVazia()):
            raise Exception("PilhaVazia")
        
        remove = self.topo
        self.topo = self.topo.prox
        self.tam -= 1
        return remove.valor


class ArvoreBinaria:
    """ Define o TAD ArvoreBinaria, uma arvore com apenas dois
    filhos, nomeados de esquerdo e direito.
    :atrib valor: contido neste no
    :atrib filhoEsq: outra ArvoreBinaria
    :atrib filhoDir: outra ArvoreBinaria
    """
    def __init__(self,valor):
        """ Metodo construtor.
        :param valor: que sera armazenado neste no
        """
        self.valor = valor
        self.filhoEsq = None
        self.filhoDir = None

    def __str__(self, nivel=0):
        """ Metodo para definir o print do objeto.
        :return: a string de como eh o print
        """
        if (self == None):
            return
        else:
            saida = "  "*nivel + str(self.valor) + "\n"
            if (self.filhoEsq != None):
                saida += self.filhoEsq.__str__(nivel+1)
            if (self.filhoDir != None):
                saida += self.filhoDir.__str__(nivel+1)
            return saida

    def insereEsq(self, val_filho):
        """ Metodo para adicionar o no com valor 'val_filho' no filho esquerdo.
        :param val_filho: valor do no
        """
        filho = ArvoreBinaria(val_filho)
        self.filhoEsq = filho

    def insereDir(self, val_filho):
        """ Metodo para adicionar o no com valor 'val_filho' no filho direito.
        :param val_filho: valor do no
        """
        filho = ArvoreBinaria(val_filho)
        self.filhoDir = filho

    def printPreOrdem(self):
        """ Metodo que usa o percurso pre-ordem para imprimir todos os elementos da arvore."""
        print(self.valor)

        if (self.filhoEsq != None):
            self.filhoEsq.printPreOrdem()
        
        if (self.filhoDir != None):
            self.filhoDir.printPreOrdem()    

    def busca(self, valor):
        """ Metodo para buscar "valor" na arvore, usando percurso pre-ordem.
        :param valor: que sera buscado
        :return: ArvoreBinaria c/ "valor", se "valor" estiver aqui; None, caso contrario
        """
        if (self.valor == valor):
            return self
        
        if (self.filhoEsq != None):
            auxE = self.filhoEsq.busca(valor)
            if (auxE != None and auxE.valor == valor):
                return auxE
        
        if (self.filhoDir != None):
            auxD = self.filhoDir.busca(valor)
            if (auxD != None and auxD.valor == valor):
                return auxD
        
        return None

    def updateNo(self, no, novo_valor):
        """ Metodo para atualizar o valor de algum no desta arvore.
        :param no: valor que ainda esta armazenado na arvore
        :param novo_valor: que substituira o valor de 'no'
        """
        aux = self.busca(no)
        if (aux == None): raise Exception('NoNaoEncontrado')
        aux.valor = novo_valor
        return


class Conjunto:
    """ Define o TAD conjunto, uma respresentacao para conjuntos numericos.
    :atrib nome: o nome do conjunto
    :atrib valores: uma lista sequencial com os valores
    """
    def __init__(self, nome, valores=[]):
        """ Metodo construtor.
        :param nome: o nome do conjunto
        :param valores: uma lista com os valores
        """
        self.nome = nome
        self.valores = valores
        self.organiza()

    def __str__(self):
        """ Metodo para definir o print do objeto.
        :return: a string de como eh o print
        """
        if (self.valores == []):
            return "conjunto vazio"

        #construcao da string
        aux = '{' + str(self.valores[0])
        for num in range(1, len(self.valores)):
            aux += ', ' + str(self.valores[num])

        return aux + '}'

    def adicionaValor(self, valor):
        """ Metodo para adicionar um valor ao conjunto.
        :param valor: que sera adicionado
        """
        if (self.valores == []):
            #se estiver vazio, apenas coloque o valor
            self.valores.append(valor)
            return

        #se nao, colocar na posicao correta, em ordem crescente
        for i in range(len(self.valores)):
            #verifica se ha um numero maior que 'valor'
            if (valor < self.valores[i]):
                #adiciona 'valor' antes dele
                aux = self.valores[:i] + [valor]
                self.valores = aux + self.valores[i:]
                return

        #se nao for antes do ultimo, so pode ser depois
        self.valores.append(valor)
        return

    def organiza(self):
        """ Metodo para organizar o conjunto em ordem crescente,
        usando o algoritmo bubblesort.
        """
        mudou = True
        i = len(self.valores) - 1
        
        while (i > 0 and mudou):
            mudou = False
            for j in range(i):
                #percorra o vetor, colocando o maior valor no final
                if (self.valores[j] > self.valores[j+1]):
                    self.valores[j], self.valores[j+1] = self.valores[j+1], self.valores[j]
                    mudou = True
            i -= 1
        return

    def uniao(self, other):
        """ Metodo para unir dois conjuntos.
        :param other: Conjunto - que sera unido com este
        :return: Conjunto - resultado da uniao
        """
        aux = Conjunto(None, self.valores[:]) #copia de self

        for numB in other.valores:
            #verifica se ha valores repetidos
            if (numB not in aux.valores):
                #adiciona se for novo
                aux.adicionaValor(numB)

        return aux

    def interseccao(self, other):
        """ Metodo para achar a interseccao de dois conjuntos.
        :param other: Conjunto - necessario para a interseccao
        :return: Conjunto - resultado da interseccao
        """
        aux = Conjunto(None, []) #objeto que sera retornado

        for numB in other.valores:
            #verifica se ha repetidos
            if (numB in self.valores):
                #adiciona se for repetido
                aux.adicionaValor(numB)

        return aux

    def diferenca(self, other):
        """ Metodo para achar a diferenca de dois conjuntos.
        :param other: Conjunto - que sera subtraido deste
        :return: Conjunto - resultado da diferenca
        """
        #copia de self e de other
        copiaS = Conjunto(None, self.valores[:])
        copiaO = Conjunto(None, other.valores[:])
        
        if (self.valores == [] or other.valores == []):
            #se qualquer um dos conjuntos estiver vazios,
            #nao ha o que subtrair
            return copiaS

        elif (copiaS.valores[-1] < copiaO.valores[0]):
            #por estarem em ordem crescente,
            #nao ha mais elementos em comum
            return copiaS
        else:
            firstO = copiaO.valores.pop(0)
            #procura se ha este item em copiaA,
            #de tras para frente
            for a in range(len(copiaS.valores)-1, -1, -1):
                if (firstO == copiaS.valores[a]):
                    copiaS.valores.pop(a)
                    #retira-o, se existir
                    break

        return copiaS.diferenca(copiaO)
    

def constroiArvore(frase):
    """ Funcao para construir uma arvore binaria a partir de uma frase dada.
    :param frase: string - que representa a arvore
    :return: ArvoreBinaria - o objeto resultante
    """
    #eh uma funcao recurisa que separa a frase e constroi as arvores binarias

    NomeConj = True #condicao de parada da recursao
    for char in frase:
        #se 'frase' possuir um desses caracteres, entao nao eh o nome de um conjunto
        if (char in ["(", "|", "&", "-", ")"]):
            NomeConj = False
            break
    if (NomeConj):
        #retorna como arvore o nome de conjunto
        return ArvoreBinaria(frase)

    aux = ArvoreBinaria(None) #arvore que sera retornada
    nivel=-1 #serve para saber a localizacao do no pai

    for char in range(len(frase)):
        if (frase[char] == '('):
            #os parenteses ajudam a localizar o no pai
            nivel += 1
            continue
        elif (frase[char] == ')'):
            nivel -= 1
            continue

        elif (nivel == 0 and frase[char] in ["|", "&", "-"]):
            #se for um desses caracteres e estiver no 'nivel=0' entao eh um no pai

            aux.valor = frase[char] #adiciona o no pai
            
            filhoEsqStr = frase[2:char-1] #separa o filho Esquerdo

            filhoDirStr = frase[char+2:-2] #separa o filho Direito 
            break
    
    #constroi os filhos
    filhoESQ = constroiArvore(filhoEsqStr)
    filhoDIR = constroiArvore(filhoDirStr)

    #e adiciona-os
    aux.filhoEsq = filhoESQ
    aux.filhoDir = filhoDIR

    return aux

def separaInput(conj_str):
    """ Funcao para separar o nome e os numeros do conjunto passado como string.
    :param conj_str: string - com o nome e os valores do conjunto
    :return: o nome do conjunto; e uma lista com os numeros
    """
    for char in range(len(conj_str)):
        #separar o nome
        if (conj_str[char] == ':'):
            name = conj_str[:char]
            nums = conj_str[char+1:] + ' ' #eh so para garantir que o algoritmo abaixo funcione
            break

    list_nums = []
    i = 0
    #constroi uma lista dada a string com os numeros separados por ' '
    while (i < len(nums)):
        if (nums[i] == ' '): #acha o 1o espaco

            for j in range(i+1, len(nums)):

                if (nums[j] == ' '): #acha o 2o espaco
                    num = nums[i+1:j] #'recorta' o numero
                    list_nums.append(int(num))
                    i = j-1 #proxima iteracao ja pode comecar do 2o espaco
                    break
        i += 1

    return name, list_nums

def resultadoArvore(arvore, pilha=Pilha()):
    """ Funcao para calcular as operacoes com os conjuntos que estao armazenados em 'arvore'.
    :param arvore: com as operacoes e conjuntos
    :return: Conjunto - resultante de todas as operacoes
    """
    #basicamente, a ideia eh percorrer a arvore usando o percurso pos-ordem:
    if (arvore.filhoEsq != None):
        resultadoArvore(arvore.filhoEsq, pilha) #filhos da esquerda

    if (arvore.filhoDir != None):
        resultadoArvore(arvore.filhoDir, pilha) #filhos da direita

    if (arvore.valor == '|'): #uniao
        aux2 = pilha.desempilha()
        aux1 = pilha.desempilha()
        pilha.empilha(aux1.uniao(aux2))

    elif(arvore.valor == '&'): #interseccao
        aux2 = pilha.desempilha()
        aux1 = pilha.desempilha()
        pilha.empilha(aux1.interseccao(aux2))

    elif(arvore.valor == '-'): #diferenca
        aux2 = pilha.desempilha()
        aux1 = pilha.desempilha()
        pilha.empilha(aux1.diferenca(aux2))
    else:
        pilha.empilha(arvore.valor)

    return pilha.topo.valor

#main:
arvore_str = input().strip("\r") 
binTree = constroiArvore(arvore_str)
print(binTree)

while (True):
    conj = input().strip("\r")
    if (conj == 'X'): break
    name, lista = separaInput(conj)
    binTree.updateNo(name, Conjunto(name, lista))

resultado = resultadoArvore(binTree)
print(resultado)

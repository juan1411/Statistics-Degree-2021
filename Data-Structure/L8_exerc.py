"""
Lista 8
Componentes do grupo :
NUSP : 11912787

  Programa que cria uma arvore de decisoes a partir de dados
passados pelo usuario e busca um resultado dentro dela, dado
as instrucoes, as condicoes a serem seguidas.
  Assim, o TAD Arvore implementado eh parecido com o que esta
disponivel no e-Disciplinas, com a adicao do atributo 'condicao'
e dos metodos 'insereRamos' (para adicionar varios filhos) e
'buscaNo' (para acessar um no especifico).
  E funcoes auxiliares tambem foram necessarias para fazer um
'tratamento' dos dados passados pelo usuario e, de fato, buscar
uma resposta dentro da arvore.
"""

class Arvore:
    """
    Define o TAD Arvore de Decisao, que representa um unico no
    com sua condicao, seu valor e seus 'no filhos' associados.
    :param condicao: qual a condicao para chegar neste no
    :param valor: valor a ser guardado neste no
    :atrib cond: condicao armazenada
    :atrib valor: valor armazenado
    :atrib filhos: vetor de 'arvores filhas' deste no
    """
    def __init__(self, condicao, valor):
        self.cond = condicao
        self.valor = valor
        self.filhos = []
        
    def __str__(self, nivel=0):
        """
        Metodo para montar a string para impressao da arvore.
        :param nivel: inteiro - representa a distancia da raiz
        :return: a string para impressao
        """
        if (self == None):
            return
        else:
            saida = "  "*nivel + str(self.valor)
            
            if (nivel != 0): #a raiz nao tem condicao
                saida += f' | cond: {self.cond}' 

            saida += "\n"
            for filho in self.filhos:
                saida += filho.__str__(nivel+1)
            return saida

    def insere(self,filho):
        """
        Metodo para inserir um no filho nesta arvore.
        :param filho: arvore a ser inserida
        """
        self.filhos.append(filho)


    def insereRamos(self, no, ramos):
        """
        Metodo para inserir varios 'nos filhos' em um no
        especifico.
        :param no: em qual no os filhos serao inseridos
        :param ramos: vetor de 'Arvores'
        """
        aux = self.buscaNo(no) #procura pelo no especifico

        if (aux == None):
            raise Exception('NoNaoEncontrado')
        
        for r in ramos: #de fato insere
            aux.insere(r)


    def buscaNo(self, no):
        """
        Metodo para buscar um no especifico nesta arvore.
        :param no: valor do no buscado
        :return: o no, se encontrar; None, caso contrario.
        """
        if (self.valor == no):
            return self #retorne se encontrar

        for filho in self.filhos:
            #se nao, procure entre os filhos
            aux = filho.buscaNo(no)
            if (aux != None and aux.valor == no):
                return aux
        return None


def analisaInput(frase):
    """
    Funcao auxiliar para separar a 1a entrada de dados.
    :param frase: string - a ser separada
    :return: valor do no pai
    :return: vetor de arvores que serao filhas de 'pai'
    """
    for p in range(len(frase)):
        if (frase[p] == ':'):
            no = frase[:p] #separa o valor do no pai
            ramos_str = frase[p+2:] #e as filhas
            break

    #separa a string em uma lista de nos filhos
    ramos_str = ramos_str.split('; ')
    ramos = []

    for cEv in ramos_str:
        for p in range(len(cEv)):
            if (cEv[p] == ','):
                cond = cEv[:p] #separa a condicao
                valor = cEv[p+2:] #e o valor, de cada filha
                ramos.append( Arvore(cond, valor) )
                #adiciona a arvore filha na lista para o return
                break        
    return no, ramos


def analisaCond(frase):
    """
    Funcao auxiliar para separar a 2a entrada de dados.
    :param frase: string - a ser separada
    :return: vetor de tuplas com o valor de um no
        e condicao a ser seguida
    """
    aux = frase.split('; ') #separa as condicoes
    instrucoes = []
    
    for vEc in aux:
        for p in range(len(vEc)):
            if (vEc[p] == ':'):
                valor = vEc[:p] #separa o valor
                cond = vEc[p+2:] #e a condicao, de cada uma
                instrucoes.append( (valor, cond) )
                #adiciona a tupla na lista para o return
                break
    return instrucoes


def buscaEmArvore(arvore, instrucao):
    """
    Funcao auxiliar para buscar uma resposta dentro de
    uma arvore, dada as instrucoes a serem seguidas.
    :param arvore: Arvore - na qual ocorrera a busca
    :param instrucoes: lista de tupla - com as intrucoes
    :return: o resultado buscado
    """
    if (len(instrucoes) == 0 or len(arvore.filhos) == 0):
        #se nao houver mais instrucoes
        #ou o no nao possuir filhos
        return arvore.valor
        
    for num in range(len(instrucoes)):
        #procure pelo no raiz nas instrucoes
        if (instrucoes[num][0] == arvore.valor):
            condicao = instrucoes[num][1]
            break

    instrucoes.pop(num) #deletar o no raiz

    for filho in arvore.filhos:
        #seguir a condicao passada
        if (filho.cond == condicao):
            aux = filho
            break
    #repita ate encontrar
    return buscaEmArvore(aux, instrucoes)

    
#main:
tree = None
frase = 'PASS'

while (frase != 'X'):
    if (frase != 'PASS'):
        #cria arvores filhas
        raiz, filhos = analisaInput(frase)

        if (tree == None):
            #o 1o no, a raiz, nao tem condicao
            tree = Arvore(None, raiz)
        
        #adiciona 'filhos'
        tree.insereRamos(raiz, filhos)
    
    frase = input().rstrip("\r")

print(tree)

cond = input().rstrip("\r")
instrucoes = analisaCond(cond)
resposta = buscaEmArvore(tree, instrucoes)

print(resposta)

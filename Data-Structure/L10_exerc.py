"""
Lista 10

  Programa que le um arquivo 'dicio.txt' para criar um dicionario em formato de
arvore binaria, que considera o criterio de ordem alfabetica para inserir os nos.
  Alem disso, o programa tambem espera uma entrada de dados do usuario (uma palavra
em ingles) para buscar dentro da arvore uma traducao (palavra em portugues). Caso
nao seja encontrada a palavra buscada, opcoes serao sugeridas e se nao houverem 
sugestoes, uma mensagem de 'sem sugestoes' sera exibida.
  Para isso, foi implementado o TAD Arvore Binaria de Busca, com apenas os metodos
necessario para que o programa funcione, e uma funcao auxiliar para pesquisar e
exibir as respostas corretas para as palavras pesquisadas pelo usuario.
"""

class ABB:
    """ Classe que implementa uma Arvore Binaria de Busca (ABB),
    com apenas dois filhos, nomeados de esquerdo e direito.
    :atrib valor: contido neste no
    :atrib valor2: tambem contido neste no
    :atrib filhoEsq: outra ABB
    :atrib filhoDir: outra ABB
    :regra: FilhoEsq.valor < Self.valor < FilhoDir.valor
    """
    def __init__(self,valor,valor2=None):
        """ Metodo Construtor.
        :param valor: que sera armazenado na raiz
        :param valor2: que tambem sera armazenado na raiz
        """
        self.valor = valor
        self.valor2 = valor2
        self.filhoEsq = None
        self.filhoDir = None

    def __str__(self,nivel=0):
        """ Metodo para definir o print do objeto, usando o percurso pre-ordem.
        :return: a string de como eh o print
        """
        if (self == None):
            if (nivel == 0):
                return "A arvore esta vazia!"
            return ""
        
        saida = "  "*nivel + str(self.valor) + "\n"
        
        if (self.filhoEsq != None):
            saida += self.filhoEsq.__str__(nivel+1)
        
        if (self.filhoDir != None):
            saida += self.filhoDir.__str__(nivel+1)
        return saida

    def insere(self,valor,valor2=None):
        """ Metodo para inserir um novo no na arvore, de forma que ela continue sendo uma ABB.
        :param valor: que sera inserido na arvore
        :param valor2: tambem sera inserido na arvore, no mesmo No que 'valor'
        :return: False, se 'valor' ja existir na arvore
        :return: True, se ele foi inserido
        """
        if (self.valor == None):
            self.valor = valor
            self.valor2 = valor2
            return True
        
        atual = self

        while (True):
            if (valor == atual.valor):
                print(str(valor)+" ja presente na arvore!")
                return False
        
            #Para continuar sendo ABB, eh preciso inserir de modo que respeite a regra
            if (valor < atual.valor):
                if (atual.filhoEsq == None):
                    atual.filhoEsq = ABB(valor, valor2)
                    return True
                else:
                    atual = atual.filhoEsq
            else:
                if (atual.filhoDir == None):
                    atual.filhoDir = ABB(valor, valor2)
                    return True
                else:
                    atual = atual.filhoDir
    
    def busca(self,valor):
        """ Metodo para buscar "valor" na arvore, usando percurso pre-ordem.
        :param valor: que sera buscado
        :return: ABB com "valor", se "valor" estiver aqui; None, caso contrario
        """
        atual = self
        
        while (atual != None):
            if (valor == atual.valor):
               return atual
        
            if (valor < atual.valor):
               atual = atual.filhoEsq
            else:
               atual = atual.filhoDir
        
        return None

    def buscaParecida(self,palavra, nivel=0):
        """ Metodo para buscar especificamente palavras parecidas dentro da arvore,
        usando percurso pre-ordem (ou "ordem alfabetica").
        :param palavra: que sera buscada
        :return 1: frase com todas as sugestoes
        :return 2: outra frase, caso nao haja sugestoes
        """
        saida = ""
        tam = len(palavra)
        
        if (self.filhoEsq != None):
            saida += self.filhoEsq.buscaParecida(palavra, nivel+1)

        if (tam <= len(self.valor) and palavra == self.valor[:tam]):
            saida += f'    {self.valor}: {self.valor2}\n'
        
        if (self.filhoDir != None):
            saida += self.filhoDir.buscaParecida(palavra, nivel+1)

        return saida


def pesquisarTraducao(palavra, dicionario):
    """ Funcao auxiliar para encontrar a traducao de'palavra' em 'dicionario' e
    sugerir uma palavra buscada com seu significado caso nao exista exatamente 'palavra'.
    :param palavra: string - que sera buscada
    :param dicionario: ABB - ja contendo as palavras e traducoes
    """
    #procurando exatamente 'palavra'
    resp = dicionario.busca(palavra)
    if (resp != None):
        print(resp.valor2)
        return

    #procurando uma palavra parecida
    resp = dicionario.buscaParecida(palavra)
    if (len(resp) == 0):
        print("termo nao encontrado e sem sugestoes")
    else:
        print("termo nao econtrado, abaixo os termos sugeridos:\n"+resp, end="")
    return
    
    
# Main:
arq = open('dicio.txt', 'r')

#Construcao do Dicionario
dicionario = None
for frase in arq:
    #lendo o arq
    for char in range(len(frase)):
        #separando as palavras
        if (frase[char] == ","):
            ingles = frase[:char]
            ptBR = frase[char+1:] 
            break

    #adicionando ao dicionario
    if (ptBR[-1] == "\n"):
        ptBR = ptBR[:-1] #para retirar o '\n' do final da palavra
        
    if (dicionario == None):
        dicionario = ABB(ingles, ptBR)
    else:
        dicionario.insere(ingles, ptBR)
    
arq.close()
print(dicionario)

while(True):
    palavra = input().strip('\r')
    if (palavra == "X"): break
    pesquisarTraducao(palavra, dicionario)

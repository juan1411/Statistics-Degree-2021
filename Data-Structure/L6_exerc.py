""" Lista 6
    
  Programa que, dada uma chave, criptografa uma mensagem do usuario com o metodo
de cesar e também coloca '*' a cada tres caracteres.
  Como pedido, foram criados dois TAD no formato de listas encadeadas: um para a mensagem
e outro para a chave (esta sendo uma lista circular), alem de um terceiro para cada no da lista.
  E visto que e necessario existir uma mensagem para, entao, ser criptografada, optei por
criar um metodo no TAD 'Mensagem' com esta funcao de criptografia, sendo requisitada a chave.
  Alem disso, criei outras funcoes que facilitavam para debbugar ou acompanhar o codigo.
"""

#Representacao dos Nós
class Node:
    """TAD que representa um unico item de uma lista encadeada.
    param
        data: object   - o que sera armazenado dentro do objeto
        point: Node    - indicacao de para onde este objeto ira apontar
    atrib
        valor: object  - o valor contido dentro do objeto
        ponteiro: Node - indica para qual outro no este aponta
    """
    def __init__(self, data, point=None):
        self.valor = data
        self.ponteiro = point

    def __str__(self):
        '''Como sera o objeto quando for printado'''
        return f'{self.valor}'


#TADs
class Mensagem:
    """TAD para uma mensagem no formato de lista encadeada, cada
    caracter representa um no da lista.
    param
        mensagem: string - texto que sera armazenado
    atrib
        inicio: Node     - indica o primeiro no da lista
        tam: inteiro     - tamanho da lista
    """
    def __init__(self, mensagem):
        aux = str(mensagem)
        self.inicio = None
        self.tam = 0

        #criacao da lista
        for caracter in aux:
            self.add_char_fim(caracter)

    def add_char_fim(self, new_char):
        '''Metodo para adicionar um novo caracter ao final da lista.
        param new_char: string - caracter a ser adicionado
        '''
        char = str(new_char)
        #novo no apontando para None
        new_node = Node(char)
        
        #caso a lista esteja vazia, ela deve comecar neste novo no
        if (self.tam == 0):
            self.inicio = new_node
        else:
            #do contrario, o ultimo precisa apontar para o novo
            node_aux = self.__getitem__(self.tam - 1)
            node_aux.ponteiro = new_node

        self.tam += 1
        return

    def __getitem__(self, i):
        '''Metodo para acessar os nodes armazenados (apenas indices positivos).
        param i: inteiro - indica qual o indice buscado, comeca em zero'''
        if (i >= self.tam) or (i < 0): raise IndexError
        atual = self.inicio
        indice_aux = 0 #um indice numerico igual na estrutura list

        while (indice_aux != i):
            #percorre toda a lista ate encontrar o node que seria o i-esimo item 
            atual = atual.ponteiro
            indice_aux += 1

        return atual

    def cripto_cesar(self, chave):
        '''Metodo para usar a criptografia de cesar nesta mensagem.
        param
            chave: object - literalmente a chave para a criptografia
        return: nova mensagem ja criptografada
        '''
        chv = Chave(chave)
        cript_msg = ''
        
        for i in range(self.tam):
            cript_msg += chr( ord(self[i].valor) + chv[i].valor )
            if ( (i+1)%3 == 0):
                cript_msg += '*'

        return cript_msg


class Chave:
    """TAD para a chave de criptografia no formato de lista circular.
    param
        chave: object - chave de cesar para a criptografia
    atrib
        inicio: Node  - indica o primeiro no da lista
        tam: inteiro  - tamanho da lista
    """
    def __init__(self, chave):
        aux = str(chave)
        self.inicio = None
        self.tam = 0

        #criacao da lista circular
        for char in aux:
            new_node = Node(int(char))

            #caso a lista esteja vazia, ela deve comecar neste novo no
            if (self.tam == 0):
                self.inicio = new_node
            else:
                #do contrario, o ultimo precisa apontar para o novo
                node_aux = self.__getitem__(self.tam -1)
                node_aux.ponteiro = new_node

            self.tam += 1
            new_node.ponteiro = self.inicio #sempre o ultimo aponta para o comeco

    def __getitem__(self, i):
        '''Metodo para acessar os nodes armazenados (apenas indices positivos).
        param i: inteiro - indica qual o indice buscado, comeca em zero'''
        if (self.tam == 0) or (i < 0): raise IndexError
        else:
            i = i % self.tam
            node_aux = self.inicio
            indice_aux = 0

            while (indice_aux != i):
                node_aux = node_aux.ponteiro
                indice_aux += 1

            return node_aux


#Main:
def executavel():
    "Funcao principal que recebe os dados e printa a resposta"
    mensagem = input().strip('\r')
    chave = input().strip('\r')

    m = Mensagem(mensagem)
    msg_saida = m.cripto_cesar(chave)

    print(msg_saida)


executavel()

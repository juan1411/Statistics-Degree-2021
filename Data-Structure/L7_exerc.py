"""
Lista 7

 Programa que simula um espaco 2D no qual o usuario eh
capaz de, atravez de comandos digitados pelo terminal,
movimentar um '*' presente neste ambiente.
 Para armazenar cada comando foi criado o TAD Pilha e o
TAD No, porem nao foram implementados todos os metodos
comuns destas estruturas, apenas os necessarios.
 Alem disso, duas classes extras foram criadas para uma
melhor organizacao de codigo; a primeira, 'Jogo', contem
atributos e metodos relacionados ao espaco 2D, enquanto
que a segunda, 'Observer', contem metodos para 'interagir'
com o usuario e efetivamente guardar uma pilha de comandos,
assim como analisa-los e responder de acordo com o que
foi requisitado.
"""


class No:
    """
    Define a classe No, que armazena um elemento da lista
    que sera usada para criar a pilha.
    :param valor: valor que sera armazenado
    :atrib prox: indica o proximo No da pilha
    """
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Pilha:
    """
    Define a classe a Pilha, que representa o TAD pilha,
    usando uma lista encadeada.
    :atrib tam: tamanho da pilha
    :atrib topo: ultimo elemento adicionado
    """
    def __init__(self):
        self.tam = 0
        self.topo = None

    def __str__(self):
        """
        Monta uma string para impressao da pilha, com os
        elementos separados por "->".
        :return: a string montada 
        """
        atual = self.topo
        saida = ""
        while (atual):
            saida += str(atual.valor) + "->"
            atual = atual.prox
        return saida

    def estaVazia(self):
        """
        Metodo que indica se a pilha esta vazia ou nao.
        :return: True, se estiver vazia
        :return: False, caso contrario
        """
        if (self.tam == 0):
            return True
        return False

    def empilha(self, valor):
        """
        Metodo para inserir um novo elemento no topo da pilha.
        :param valor: valor que sera armazenado
        """
        novo = No(valor)
        novo.prox = self.topo
        self.topo = novo
        self.tam += 1

    def desempilha(self):
        """
        Metodo para retirar o elemento no topo da pilha.
        :return: o elemento no topo
        :exception: "PilhaVazia", se a pilha estiver vazia
        """
        if (self.estaVazia()):
            raise Exception("PilhaVazia")
        
        remove = self.topo
        self.topo = self.topo.prox
        self.tam -= 1
        return remove.valor


class Jogo:
    """
    Define a classe Jogo, responsavel por lidar com tudo
    relacionado ao tabuleiro.
    :atrib tab: vetor que representa o tabuleiro
    :atrib pos_jogador: numero da posicao de '*' no vetor tab
    """
    def __init__(self):
        self.tab = ['.','.','.','.','.','.','.','.',
                    '.','.','.','.','.','.','.','.',
                    '*','.','.','.','.','.','.','.']
        self.pos_jogador = 16

    def printTab(self):
        """
        Metodo para imprimir o tabuleiro.
        """
        for i in range(len(self.tab)):
            print(self.tab[i], end='')
            if ((i+1) %8 == 0):
                #a cada 8 elementos, ha uma quebra de linha
                print()
        print()

    def moverJogador(self, ds):
        """
        Metodo para alterar a posicao de '*' no tabuleiro.
        :param ds: deslocamento de '*' no vetor tab
        """
        self.tab[self.pos_jogador] = '.'
        self.pos_jogador += ds
        self.tab[self.pos_jogador] = '*'
    

class Observer:
    """
    Define a classe Observer, responsavel pela entrada, analise
    e saida de dados.
    :atrib atualCMD: pilha com os comandos relevantes salvos
    :atrib undoCMD: pilha com os comandos 'undos'
    """
    def __init__(self):
        #todos os comandos de movimento sao salvos aqui
        self.atualCMD = Pilha()
        #para cada comando 'undo', esta pilha recebe um elemento
        self.undoCMD = Pilha()
        self.jogo = Jogo()

    def start(self):
        """
        Metodo que define o loop para o funcionamento do 'jogo'
        e realiza a entrada e saida de dados.
        """
        continuar = True
        while (continuar):
            try:
                self.jogo.printTab()
                cmd = input().strip('\r')
                self.analisaCMD(cmd)
                self.atualCMD.empilha(cmd)
            except StopIteration:
                continuar = False
            except Exception as e:
                #print(e)
                pass

    def analisaCMD(self, cmd):
        """
        Metodo que analisara a entrada de dados.
        :param cmd: comando passado pelo usuario
        """
        listaCmds = ['sobe', 'desce', 'dir',
                 'esq', 'undo', 'redo']
        
        if (cmd not in listaCmds):
            print('comando invalido')
            raise Exception("CmdInvalido")

        elif (cmd == 'undo'):
            self.undo()
            raise Exception("NaoAddEsteCMD")

        elif (cmd == 'redo'):
            self.redo()
            raise Exception("NaoAddEsteCMD")

        else:
            #se foi digitado um comando de movimento, entao
            #a pilha undoCMD precisa ficar vazia
            if (not self.undoCMD.estaVazia()):
                self.undoCMD = Pilha()
            self.cmdsMovimento(cmd)

    def cmdsMovimento(self, cmd):
        """
        Metodo que ordenara o movimento de '*' no
        tabuleiro de acordo com o comando passado.
        :param cmd: comando passado pelo usuario
        """
        pos_jogador = self.jogo.pos_jogador
        #cada condicional verifica se o movimento pode
        #ser realizado no tabuleiro atual.
        if (cmd == 'sobe') and (pos_jogador > 7):
            self.jogo.moverJogador(-8)
            return
            
        elif (cmd == 'desce'):
            if (pos_jogador < 16):
                self.jogo.moverJogador(8)
                return
                
            elif (pos_jogador == 16):
                #print("Saindo...")
                raise StopIteration
            
        elif (cmd == 'dir') and ((pos_jogador +1)%8 != 0):
            self.jogo.moverJogador(1)
            return
            
        elif (cmd == 'esq') and (pos_jogador%8 != 0):
            self.jogo.moverJogador(-1)
            return
        else:
            raise Exception("NaoPodeMover")

    def undo(self):
        """
        Metodo para lidar com o comando 'undo'.
        """
        if (self.atualCMD.estaVazia()):
            print("nao eh possivel desfazer\n")
            raise Exception("UndoError-EmptyList")

        #adicionar o ultimo comando em undoCMD
        uCMD = self.atualCMD.desempilha()
        self.undoCMD.empilha(uCMD)
        #agr eh preciso fazer o oposto dele:
        troca = {'dir':'esq', 'esq':'dir',
                 'sobe':'desce', 'desce':'sobe'}
        oposto = troca[uCMD]
        self.cmdsMovimento(oposto)
    
    def redo(self):
        """
        Metodo para lidar com o comando 'redo'.
        """
        if (self.undoCMD.estaVazia()):
            print("nao eh possivel refazer\n")
            raise Exception("RedoError-EmptyList")

        #refazer o ultimo comando de undoCMD
        reCMD = self.undoCMD.desempilha()
        self.cmdsMovimento(reCMD)
        #e readiciona-lo em atualCMD
        self.atualCMD.empilha(reCMD)
            

#Main
GM = Observer()
GM.start()

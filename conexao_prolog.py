import subprocess
import time
import random
import select
import os

"""
time atual = 0
número da camisa = 1
posição = 2
cor primária do time atual = 3
cor secundário do time atual = 4
pé dominante = 5
título mais relevante conquistado = 6
jogou na seleção = 7
jogou na europa = 8
nacionalidade = 9
"""

class Conexao:

    # Esse comando vai apenas inicializar o terminal no qual vamos nos comunicar com o prolog
    def __init__(self, arquivo_dados, num_perguntas):

        self.num_perguntas = num_perguntas
        self.possiveis_jog = list()
        self.jog_lista_negra = list()
        self.possiveis_perguntas = list(range(self.num_perguntas))

        # Verificando se o arquivo prolog existe, senão existir, o programa encerra
        if not os.path.exists(arquivo_dados):
            print(f"Arquivo não encontrado: {arquivo_dados}")
            exit(1)

        # Inicializando o terminal que usaremos para nos comunicar com o prolog
        self.banco_dados = subprocess.Popen(
                           ['swipl', '-q', '-s', arquivo_dados],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True,
                           bufsize=1,
                           )
        
        # Tempo para inicialização o subprocess, para não dar erro
        time.sleep(0.5)

    # Essa função vai se comunicar com o prolog para fazer a entrada de dados por ele
    def gerarPergunta(self):
        # Geramos uma pergunta aleatória
        pergunta = random.choice(self.possiveis_perguntas)

        # Removendo-a para não ser escolhida de novo
        self.possiveis_perguntas.remove(pergunta)

        # Função que mandará o prolog fazer a pergunta e salvará os dados
        requisicao = 'pergunta' + str(pergunta) + 'x'

        if pergunta == 0:
            requisicao += '(time, Time).\n'
        elif pergunta == 1:
            requisicao += '(camisa, CamisaStr).\n'
        elif pergunta == 2:
            requisicao += '(posicao, Posicao).\n'
        elif pergunta == 3:
            requisicao += '(cor1, Cor1).\n'
        elif pergunta == 4:
            requisicao += '(cor2, Cor2).\n'
        elif pergunta == 5:
            requisicao += '(pe, Pe).\n'
        elif pergunta == 6:
            requisicao += '(titulo, Titulo).\n'
        elif pergunta == 7:
            requisicao += '(selecao, Selecao).\n'
        elif pergunta == 8:
            requisicao += '(europa, Europa).\n'
        elif pergunta == 9:
            requisicao += '(nacionalidade, Nacionalidade).\n'

        # Esse código manda a pergunta pela primeira vez para o código, então o responde com uma pergunta qualquer,
        # apenas para receber o output com a pergunta que será feita, então ele recebe o output e printa a pergunta
        # no terminal python e após a resposta, ele realmente preenche com a resposta dada pelo usuário.
        self.banco_dados.stdin.write(requisicao)
        self.banco_dados.stdin.flush()
        time.sleep(0.1)
        self.banco_dados.stdin.write('a\n')
        solicitacao = self.ler_saida()

        # Retirando o caracterer que identifica a função que não salva
        requisicao = requisicao.replace('x', '')

        self.banco_dados.stdin.write(requisicao)
        self.banco_dados.stdin.flush()
        time.sleep(0.1)

        # Serve para fazer a interação entre o que sairá do terminal do prolog com o que será escrito no
        # terminal do python
        solicitacao = solicitacao[0].split('*')[0]
        resposta = input(solicitacao)

        self.banco_dados.stdin.write(resposta + '\n')
        self.banco_dados.stdin.flush()
        self.ler_saida()

    def consulta(self):
        # Após a perguntar ser gerada e feita, temos que pesquisar os possíveis jogadores a partir do dados
        # gerados pelas perguntas
        self.banco_dados.stdin.write('consulta_jogador(Nome).\n')
        self.banco_dados.stdin.write('.\n')
        self.banco_dados.stdin.flush()
        time.sleep(0.1)

        # Recebendo o retorno da requisição, e verificando se ele é vazio
        retorno = self.ler_saida()

        # Tratando o retorno para torná-lo uma string legível
        retorno = retorno[0]
        retorno = retorno.split('[')[1]
        retorno = retorno.split(']')[0]

        if retorno == '':
            self.possiveis_jog = []
        else:
            self.possiveis_jog = retorno.split(',')
            self.possiveis_jog = [ele for ele in self.possiveis_jog if ele not in self.jog_lista_negra]

    # 0 => segue o funcionamento normal, 1 => Algoritmo acertou, 2 => Algoritmo deve parar
    def adivinhar(self):
        # Se for maior ele não deve tentar adivinhar
        if len(self.possiveis_jog) > 10:
            return 0
        
        # Retornando isso caso não haja nenhum jogador cumprindo as condições
        if self.possiveis_jog == []:
            return 2
        
        # Escolhendo um jogador aleatório dentre os possíveis para tentar um chute
        chute = random.choice(self.possiveis_jog)

        ganhou = input(f'O seu jogador é {chute}? (sim/nao): ')
        ganhou = ganhou.lower()

        if ganhou == 'sim':
            return 1
        else:
            # Se o único jogador que poderia ser, não foi escolhido
            if len(self.possiveis_jog) == 1:
                return 2
            else:
                # Fazendo com que o jogador que não foi escolhido, não caia de novo na pergunta
                self.jog_lista_negra.append(chute)
                return 0

    # Função para ler a saída de dsados do arquivo prolog
    def ler_saida(self):
        linhas = []
        while True:
            if not self.tem_dados_para_ler(self.banco_dados.stdout):
                break
            linha = self.banco_dados.stdout.readline()
            linha = linha.strip()
            if linha == '' or linha.startswith('?-') or linha == 'true' or linha == 'false':
                continue
            linhas.append(linha)
            if linha in ('false.', 'true.'):
                break
        return linhas
    
    # Verifica se há dados disponíveis para leitura no stdout
    def tem_dados_para_ler(self, stdout_stream):
        rlist, _, _ = select.select([stdout_stream], [], [], 0.1)  # timeout de 0.1s
        return bool(rlist)
    
    # Função principal, que vai controlar os outros métodos
    def jogar(self):
        print("Bem-vindo ao Prolog Akinator! Espero que se divirta :)")

        for i in range(self.num_perguntas):
            self.gerarPergunta()
            self.consulta()
            ganhou = self.adivinhar()

            if ganhou == 1:
                print("Oba, acertei")
                break
            elif ganhou == 2:
                print("Infelizmente, não conheço nenhum jogador essas características ;-;")
                break

        print("Obrigado por jogar!!!")
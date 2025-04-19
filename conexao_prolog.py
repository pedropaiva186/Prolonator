import subprocess
import time
import random

# Usar o "findall" do prolog, para pegar todos os jogadores de uma vez

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
        self.possiveis_perguntas = list(range(0, 10))
        self.resposta_usr = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

        # Inicializando o terminal que usaremos para nos comunicar com o prolog
        self.banco_dados = subprocess.Popen(
                           ["swipl"],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True,
                           bufsize=1
                           )

        # Conectando o terminal prolog com o arquivo que usaremos como banco de dados
        self.banco_dados.stdin.write(f'consult("{arquivo_dados}")')

        # Limpando a stream de escrita, para previnir erros
        self.banco_dados.stdin.flush()

    def gerarPergunta(self):
        # Geramos uma pergunta aleatória caso seja a primeira pergunta do jogo
        if len(self.possiveis_perguntas) == self.num_perguntas:
            # Escolhendo a aleatória
            pergunta = random.choice(self.possiveis_perguntas)
            # Removendo-a para não ser escolhida de novo
            self.possiveis_perguntas.remove(pergunta)
        else:
            # Implementar a pergunta que exclui a maior quantidade de jogadores
            print("1")

        if pergunta == 0:
            self.resposta_usr[0] = input("Digite o time atual do jogador escolhido: ")
        elif pergunta == 1:
            self.resposta_usr[1] = input("Digite o número da camisa do jogador escolhido: ")
        elif pergunta == 2:
            self.resposta_usr[2] = input("Digite a posição do jogador escolhido: ")
        elif pergunta == 3:
            self.resposta_usr[3] = input("Digite a cor primária do time do jogador escolhido: ")
        elif pergunta == 4:
            self.resposta_usr[4] = input("Digite a cor secundária do time do jogador escolhido: ")
        elif pergunta == 5:
            self.resposta_usr[5] = input("Digite o pé dominante do jogador escolhido: ")
        elif pergunta == 6:
            self.resposta_usr[6] = input("Digite o título mais relevante conquistado pelo jogador escolhido: ")
        elif pergunta == 7:
            self.resposta_usr[7] = input("Digite se o jogador escolhido jogou na seleção: ")
        elif pergunta == 8:
            self.resposta_usr[8] = input("Digite se o jogador escolhido jogou na Europa: ")
        elif pergunta == 9:
            self.resposta_usr[9] = input("Digite a nacionalidade do jogador escolhido: ")


    def consulta(self):
        self.gerarPergunta()

        print("batata")

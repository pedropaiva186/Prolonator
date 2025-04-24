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
                           bufsize=1
                           )
        
        self.ler_saida()

        # Usando esse comando para configurar a saída do prolog, para que ele exiba todos os elementos
        self.banco_dados.stdin.write("set_prolog_flag(answer_write_options, [max_depth(0)]).\n")
        self.banco_dados.stdin.flush()
        self.ler_saida()


    # Essa função vai se comunicar com o prolog para fazer a entrada de dados por ele
    def gerarPergunta(self):
        # Geramos uma pergunta aleatória
        pergunta = random.choice(self.possiveis_perguntas)

        # Removendo-a para não ser escolhida de novo
        self.possiveis_perguntas.remove(pergunta)

        # Função que mandará o prolog fazer a pergunta e salvará os dados
        requisicao = 'pergunta' + str(pergunta)

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

        self.banco_dados.stdin.write(requisicao)
        self.banco_dados.stdin.flush()
        time.sleep(0.1)

        print(requisicao)

        # Serve para fazer a interação entre o que sairá do terminal do prolog com o que será escrito no
        # terminal do python
        solicitacao = self.ler_saida()
        resposta = input(solicitacao)

        self.banco_dados.stdin.write(resposta)
        self.ler_saida()

    def consulta(self):
        self.gerarPergunta()

        # Após a perguntar ser gerada e feita, temos que pesquisar os possíveis jogadores a partir do dados
        # gerados pelas perguntas
        self.banco_dados.stdin.write('consulta_jogador(X).\n')

        # Recebendo o retorno da requisição, e verificando se ele é vazio
        retorno = self.ler_saida()
        if retorno == ['true.']:
            print('Nenhum jogador encontrado com tais características.')

        print(retorno)

    # Função para ler a saída de dsados do arquivo prolog
    def ler_saida(self):
        linhas = []
        while True:
            if not self.tem_dados_para_ler(self.banco_dados.stdout):
                break
            linha = self.banco_dados.stdout.readline()
            linha = linha.strip()
            if linha == '' or linha.startswith('?-'):
                continue
            linhas.append(linha)
            if linha in ('false.', 'true.'):
                break
        return linhas
    
    # Verifica se há dados disponíveis para leitura no stdout
    def tem_dados_para_ler(self, stdout_stream):
        rlist, _, _ = select.select([stdout_stream], [], [], 0.1)  # timeout de 0.1s
        return bool(rlist)
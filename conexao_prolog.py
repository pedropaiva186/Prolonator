import subprocess
import time

class Conexao:

    # Esse comando vai apenas inicializar o terminal no qual vamos nos comunicar com o prolog
    def __init__(self):
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
        self.banco_dados.stdin.write('consult("/home/pedro-paiva/Documents/Arquivos_de_Estudos/' \
                        'Projetos Programação/Projetos Python/projeto_akinator_prolog/' \
                        'banco_de_dados_jogadores.pl")')

        # Limpando a stream de escrita, para previnir erros
        self.banco_dados.stdin.flush()
        
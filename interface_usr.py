from conexao_prolog import Conexao

# Caminho para o arquivo prolog
caminho_bd = "caminho"
# Número de perguntas que serão feitas
num_perguntas = 0

jogo = Conexao(caminho_bd, num_perguntas)
jogo.jogar()
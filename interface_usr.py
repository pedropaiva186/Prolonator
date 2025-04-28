from conexao_prolog import Conexao

# Caminho para o arquivo prolog
caminho_bd = "/home/pedro-paiva/Documents/Arquivos_de_Estudos/Projetos Programação/Projetos Python/projeto_akinator_prolog/banco_de_dados_jogadores.pl"
# Número de perguntas que serão feitas
num_perguntas = 10

jogo = Conexao(caminho_bd, num_perguntas)
jogo.jogar()
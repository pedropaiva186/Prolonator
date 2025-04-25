from conexao_prolog import Conexao

caminho_bd = "/home/pedro-paiva/Documents/Arquivos_de_Estudos/Projetos Programação/Projetos Python/projeto_akinator_prolog/banco_de_dados_jogadores.pl"

jogo = Conexao(caminho_bd, 10)
jogo.jogar()
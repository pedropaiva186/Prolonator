% A forma padrão na qual os dados ficarão dispostos será:

% jogador(nome, time atual, num_camisa, posição, cor_primária_time, cor_secundária_time, pé dominante, 
% título mais relevante conquistado, jogou na seleção, jogou na europa, nacionalidade)
% São 11 características no total

% Todas as letras normalizadas, sem acento e sem letras maiúsculas

jogador(mateus, "palmeiras", 1, "goleiro", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").
jogador(marcos_rocha, "palmeiras", 2, "lateral_direito", "verde", "branco", "direito", "libertadores", "nao", "sim", "brasileiro").
jogador(bruno_fuchs, "palmeiras", 3, "zagueiro", "verde", "branco", "direito", "libertadores_sub20", "nao", "sim", "brasileiro").
jogador(agustin_giay, "palmeiras", 4, "lateral_direito", "verde", "branco", "direito", "sulamericano_sub20", "sim", "nao", "argentino").
jogador(anibal_moreno, "palmeiras", 5, "meia", "verde", "branco", "direito", "sulamericano_sub20", "sim", "nao", "argentino").
jogador(vanderlan, "palmeiras", 6, "lateral_esquerdo", "verde", "branco", "esquerdo", "copa_sao_paulo", "nao", "nao", "brasileiro").
jogador(felipe_anderson, "palmeiras", 7, "meia", "verde", "branco", "direito", "supercopa_italia", "sim", "sim", "brasileiro").
jogador(richard_rios, "palmeiras", 8, "meia", "verde", "branco", "direito", "brasileirao", "sim", "nao", "colombiano").
jogador(vitor_roque, "palmeiras", 9, "atacante", "verde", "branco", "direito", "sulamericano_sub20", "sim", "sim", "brasileiro").
jogador(paulinho, "palmeiras", 10, "atacante", "verde", "branco", "direito", "brasileirao", "sim", "sim", "brasileiro").
jogador(bruno_rodrigues, "palmeiras", 11, "atacante", "verde", "branco", "direito", "brasileirao", "nao", "nao", "brasileiro").
jogador(mayke, "palmeiras", 12, "lateral_direito", "verde", "branco", "direito", "libertadores", "nao", "sim", "brasileiro").
jogador(micael, "palmeiras", 13, "zagueiro", "verde", "branco", "direito", "brasileirao_sub20", "nao", "sim", "brasileiro").
jogador(marcelo_lomba, "palmeiras", 14, "goleiro", "verde", "branco", "direito", "brasileirao", "nao", "sim", "brasileiro").
jogador(gustavo_gomez, "palmeiras", 15, "zagueiro", "verde", "branco", "direito", "libertadores", "sim", "sim", "paraguaio").
jogador(facundo_torres, "palmeiras", 17, "atacante", "verde", "branco", "esquerdo", "sulamericano_sub20", "sim", "nao", "uruguaio").
jogador(mauricio, "palmeiras", 18, "meia", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").
jogador(weverton, "palmeiras", 21, "goleiro", "verde", "branco", "direito", "libertadores", "sim", "sim", "brasileiro").
jogador(piquerez, "palmeiras", 22, "lateral_esquerdo", "verde", "branco", "esquerdo", "libertadores", "sim", "sim", "uruguaio").
jogador(raphael_veiga, "palmeiras", 23, "meia", "verde", "branco", "direito", "libertadores", "sim", "sim", "brasileiro").
jogador(murilo, "palmeiras", 26, "zagueiro", "verde", "branco", "direito", "brasileirao", "nao", "sim", "brasileiro").
jogador(luighi, "palmeiras", 31, "atacante", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").
jogador(emiliano_martinez, "palmeiras", 32, "meia", "verde", "branco", "direito", "libertadores_sub20", "nao", "sim", "uruguaio").
jogador(naves, "palmeiras", 34, "zagueiro", "verde", "branco", "direito", "copa_sao_paulo", "nao", "nao", "brasileiro").
jogador(fabinho, "palmeiras", 35, "meia", "verde", "branco", "direito", "copa_sao_paulo", "nao", "nao", "brasileiro").
jogador(thalys, "palmeiras", 39, "atacante", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").
jogador(allan, "palmeiras", 40, "meia", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").
jogador(estevao, "palmeiras", 41, "atacante", "verde", "branco", "esquerdo", "copa_sao_paulo", "sim", "nao", "brasileiro").
jogador(flaco_lopez, "palmeiras", 42, "atacante", "verde", "branco", "direito", "campeonato_brasileiro", "nao", "sim", "argentino").
jogador(benedetti, "palmeiras", 43, "zagueiro", "verde", "branco", "direito", "brasileirao_sub20", "nao", "nao", "brasileiro").


pergunta0(time, Time) :-
    write('Qual o time do jogador? '), read_line_to_string(user_input, Time), assertz(resposta(time, Time)).

pergunta1(camisa, CamisaStr) :-
    write('Qual o numero da camisa? '), read_line_to_string(user_input, CamisaStr),
    atom_number(CamisaStr, Camisa), assertz(resposta(camisa, Camisa)).

pergunta2(posicao, Posicao) :-
    write('Qual a posicao do jogador? '), read_line_to_string(user_input, Posicao), assertz(resposta(posicao, Posicao)).

pergunta3(cor1, Cor1) :-
    write('Qual a cor primaria do time? '), read_line_to_string(user_input, Cor1), assertz(resposta(cor1, Cor1)).

pergunta4(cor2, Cor2) :-
    write('Qual a cor secundaria do time? '), read_line_to_string(user_input, Cor2), assertz(resposta(cor2, Cor2)).

pergunta5(pe, Pe) :-
    write('Qual o pe dominante? '), read_line_to_string(user_input, Pe), assertz(resposta(pe, Pe)).

pergunta6(titulo, Titulo) :-
    write('Qual o titulo mais relevante conquistado? '), read_line_to_string(user_input, Titulo), assertz(resposta(titulo, Titulo)).

pergunta7(selecao, Selecao) :-
    write('Jogou na selecao? (sim/nao) '), read_line_to_string(user_input, Selecao), assertz(resposta(selecao, Selecao)).

pergunta8(europa, Europa) :-
    write('Jogou na europa? (sim/nao) '), read_line_to_string(user_input, Europa), assertz(resposta(europa, Europa)).

pergunta9(nacionalidade, Nacionalidade) :-
    write('Qual a nacionalidade do jogador? '), read_line_to_string(user_input, Nacionalidade), assertz(resposta(nacionalidade, Nacionalidade)).

consulta_jogador(Nome) :-
    (resposta(time, Time) ; true),
    (resposta(camisa, Camisa) ; true),
    (resposta(posicao, Pos) ; true),
    (resposta(cor1, Cor1) ; true),
    (resposta(cor2, Cor2) ; true),
    (resposta(pe, Pe) ; true),
    (resposta(titulo, Titulo) ; true),
    (resposta(selecao, Sel) ; true),
    (resposta(europa, Eur) ; true),
    (resposta(nacionalidade, Nac) ; true),
    findall(Nome, jogador(Nome, Time, Camisa, Pos, Cor1, Cor2, Pe, Titulo, Sel, Eur, Nac), Lista),
    write('Jogadores compatíveis: '), write(Lista), nl.
    
    

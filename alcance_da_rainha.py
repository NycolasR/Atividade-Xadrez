def cria_matriz(valor, num_linhas=8, num_colunas=8):
    '''
    (int, int, valor) -> matriz(lista de linhas)
    Cria e retorna ums matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é passado por parâmetro de entrada.
    '''

    matriz = []

    for i in range(num_linhas):
        linha = []
        
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
        
    return matriz



def marque_atacadas(tab):
    '''
    (matriz) -> matriz(lista de linhas)
    Identifica as coordenadas da posição da rainha e dos pontos
    de origem das diagonais e demarca as posições para as quais
    a rainha pode se mover com um 'x'.
    '''
    
    i_queen, j_queen = selecionar_coordenadas_rainha(tab)
    i_diag_desc, j_diag_desc, i_diag_asce, j_diag_asce = selecionar_coordenadas_diagonais(tab)

    # adiciona a marcação nas linhas vertical e horizontal para as quais
    # a rainha pode se mover
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if (i == i_queen or j == j_queen):
                tab = adicionar_marcacao(i, j, tab)

    # adiciona a marcação na linha diagonal decrescente na qual
    # a rainha pode se mover
    while i_diag_desc < len(tab) and j_diag_desc < len(tab[0]):
        tab = adicionar_marcacao(i_diag_desc, j_diag_desc, tab)
        i_diag_desc += 1
        j_diag_desc += 1

    # adiciona a marcação na linha diagonal ascendente na qual
    # a rainha pode se mover
    while i_diag_asce >= 0 and j_diag_asce < len(tab[0]):
        tab = adicionar_marcacao(i_diag_asce, j_diag_asce, tab)
        i_diag_asce -= 1
        j_diag_asce += 1
    
    return tab


def listar_coordenadas(tab):
    '''
    (matriz)
    Lista na stdout as coordenadas dos principais
    pontos da matriz.
    '''
    
    i_queen, j_queen = selecionar_coordenadas_rainha(tab)
    
    i_diag_desc, j_diag_desc, i_diag_asce, j_diag_asce = selecionar_coordenadas_diagonais(tab)

    print(f"Coordenadas da Rainha: ({i_queen},{j_queen})")
    print("Coordenadas da origem das Diagonais:")
    print(f"    descendente: ({i_diag_desc},{j_diag_desc})")
    print(f"     ascendente: ({i_diag_asce},{j_diag_asce})")


def posicionar_rainha(i, j, tab):
    '''
    (int, int, matriz) -> matriz(lista de linhas)
    Recebe 2 inteiros como coordenadas para a posição da rainha
    e a posiciona na matriz passada por parâmetro de entrada
    '''
    
    tab[i][j] = 'R'.center(5)
    return tab


def adicionar_marcacao(i, j, tab):
    '''
    (int, int, matriz) -> matriz(lista de linhas)
    Função usada para marcar com um 'x' na matriz 
    na posição das coordenadas (i, j) passadas por parâmetro.
    '''
    
    if (tab[i][j]).strip() != 'R':
        tab[i][j] = 'x'.center(5)

    return tab


def selecionar_coordenadas_rainha(tab):
    '''
    (matriz) -> int, int
    Retorna as coordenadas (i, j) da rainha na
    matriz do tabuleiro.
    '''
    
    i_queen = j_queen = 0
    
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if (tab[i][j]).strip() == 'R':
                i_queen, j_queen = i, j
    return i_queen, j_queen


def selecionar_coordenadas_diagonais(tab):
    '''
    (matriz) -> int, int, int, int
    Com base nas coordenadas da rainha,
    serão retornadas as coordenadas de origem das
    diagonais descrescente e crescente, respectivamente
    (i, j), (i, j).
    '''
    
    i_queen, j_queen = selecionar_coordenadas_rainha(tab)
    
    #diagonal descendente
    i_diag_desc = j_diag_desc = 0
    while i_queen > 0 and j_queen > 0 :
        i_queen -= 1
        j_queen -= 1
        
    #atribuindo coordenadas
    i_diag_desc, j_diag_desc = i_queen, j_queen

    
    i_queen, j_queen = selecionar_coordenadas_rainha(tab)
    
    #diagonal ascendente
    i_diag_asce = j_diag_asce = 0
    while i_queen < len(tab)-1 and j_queen > 0:
        i_queen += 1
        j_queen -= 1

    #atribuindo coordenadas
    i_diag_asce, j_diag_asce = i_queen, j_queen
    
    return i_diag_desc, j_diag_desc, i_diag_asce, j_diag_asce
    
    
if __name__ == "__main__":
    from random import randint as r
    
    tabuleiro = cria_matriz('     ')
    tabuleiro = posicionar_rainha(r(1, 7), r(1, 7), tabuleiro)
    tabuleiro = marque_atacadas(tabuleiro)
    for lin in tabuleiro:
        print(lin)
        print()

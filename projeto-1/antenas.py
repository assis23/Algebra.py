#Projeto1- Algebra Linear
#FRANCISCO DE ASSIS AMCHADO DOS SANTOS /  JAIME GABRIEL ALVES PEREIRA


from itertools import combinations

matriz_conectividade = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
]

def opcoes_comunicacao(l1, l2, max_retransmissoes):
    if l1 < 0 or l1 >= len(matriz_conectividade) or l2 < 0 or l2 >= len(matriz_conectividade):
        return "Índice de local de transmissão inválido."

    if l1 == l2:
        return f"Você escolheu o mesmo local de transmissão: L{l1 + 1}. Não é possível a comunicação."

    opcoes = []
    
    if matriz_conectividade[l1][l2] == 1:
        opcoes.append(f"Comunicação direta entre L{l1 + 1} e L{l2 + 1}.")

    for r in range(1, max_retransmissoes + 1):
        retransmissoes = [i for i in range(len(matriz_conectividade)) if i != l1 and i != l2 and matriz_conectividade[l1][i] == 1]
        if retransmissoes:
            combinacoes = combinations(retransmissoes, r)
            for combinacao in combinacoes:
                estacoes_retransmissoras = [f"L{estacao + 1}" for estacao in combinacao]
                opcao = f"Comunicação entre L{l1 + 1} e L{l2 + 1} com retransmissões em {', '.join(estacoes_retransmissoras)}."
                opcoes.append(opcao)

    return opcoes

local1 = int(input("Escolha o índice do primeiro local de transmissão (0, 1, 2, 3, 4): "))
local2 = int(input("Escolha o índice do segundo local de transmissão (0, 1, 2, 3, 4): "))

max_retransmissoes = int(input("Digite o número máximo de retransmissões desejado (0, 1 ou 2): "))

opcoes = opcoes_comunicacao(local1, local2, max_retransmissoes)

for opcao in opcoes:
    print(opcao)
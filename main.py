# Função que analisa o pedido efetuado
# Parâmetros:
# pedido - String com o nome do produto pedido
# cardapio - Dicionário com os produtos e seus ingredientes
# estoque - Dicionário com a lista de produtos e seus ingredientes
def fazer_pedido(pedido, cardapio, estoque):
    # Condição de saída antecipada da função
    sair = False
    # Se o pedido está no cardápio
    if pedido in cardapio:
        # Pega a lista de ingredientes do produto
        ingredientes = cardapio[pedido]
        # Análise de estoque
        for ingrediente in ingredientes:
            if estoque[ingrediente] == 0:
                print("Infelizmente acabou o", ingrediente)
                sair = True
            # Saída antecipada da função, pois o produto não foi produzido
            if sair:
                return
            # Atualiza quantidades em estoque
        for ingrediente in ingredientes:
            estoque[ingrediente] -= 1
            print("Um", pedido, "saindo no capricho!!!")
    else:
        print("Item não localizado no cardápio")


# Função de Impressão do cardápio e retorno da opção escolhida
# Parâmetros:
# cardapio - Dicionário com os produtos e seus ingredientes
# Retorno:
# opcao - String com a opção de produto escolhida ou 0 para sair
def imprimir_cardapio(cardapio):
# Impressão do cardápio
    print("****** Menu ******")
    for pedido in cardapio:
        print(pedido)
        print("******************")
        # Solicitação do pedido
    opcao = input("O que deseja pedir (0 para sair)? ")
    return opcao


# Função principal de entrada do programa
def principal():
    # Dicionário com os ingredientes no estoque
    estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    # Dicionário com os produtos ofertados e os ingredientes que compõem cada um
    cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }

    while True:
        # Chama a função de impressão do cardápio
        opcao = imprimir_cardapio(cardapio)
        if opcao == "0":
            # Sai do while e do programa
            break
        else:
            # Vai para a função de realização do pedido
            fazer_pedido(opcao, cardapio, estoque)


    # Ponto de entrada do programa
    #if __name__ == '__main__':
principal()














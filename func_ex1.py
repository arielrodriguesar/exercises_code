'''                           ------ Treino com funções ------                                   '''

'''O usuário envia a quantidade de produtos de cada tipo e pede para somar.
   Nokia = 2 Motorola G7 = 3'''

def escaneia_produto(): 
    
    contador_continua_escanearProduto = 1
    produtos = []
    quantidades = 0

    while contador_continua_escanearProduto == 1:
            quantidades = int(input("Coloque a quantidade do produto em questão: "))
            produtos.append(quantidades)
            contador_continua_escanearProduto = int (input("Mais produtos = 1\nAcabou a lista = 2\n"))
    return produtos

''' Essa seria a forma de contar decimal

def contar_decimal(lista_produtos):
    tem_decimal = 0
    lista_produtos = 
    for n in lista_produtos:
        if isinstance(n, float):
            tem_decimal += 1
    return tem_decimal
'''

def soma_de_todos_produtos_recebidas(lista_produtos):
    quantidade_produtos_aoTodo = 0
    for n in lista_produtos:
        quantidade_produtos_aoTodo += n
    return quantidade_produtos_aoTodo


'''Try escaneará o produto, se tiver decimal vai dar erro, assim executará o execpt'''
try:
    produtos_escaneados = escaneia_produto()
    
    ''' Como o python entende o input como str, nunca funcionaria o except personalisado. Eu não conseguiria ler int e depois float 
    de forma separada, sem tipar a lista. Teria de criar uma função para validar ponto ou vírgula. 
    É um trabalho inprodutivo, mas pesquisei sobre except personalisado, pois surgiu a ideia e queria saber como funciona, 
    ficando então como pesquisa para outros códigos que o necessitem. 

    produtos_escaneados_verificados_decimal =  contar_decimal(produtos_escaneados)
    
    if produtos_escaneados_verificados_decimal >= 1:
        raise ErroDecimal
    elif produtos_escaneados_verificados_decimal == 0:
        print(f"A quantidade de produtos somados é {soma_de_todos_produtos_recebidas(produtos_escaneados)}")
    '''
    print(f"A quantidade de produtos somados é {soma_de_todos_produtos_recebidas(produtos_escaneados)}.")

except ValueError:
     print("Você digitou um decimal, não um inteiro.")

finally:

    print("Obrigado pela preferência.")



'''                           --------- Comentário ---------

O treino me fez ver que a melhor forma de potencializar o uso da ideia, seria tratar
esse tipo de erro dentro da função de escaneamento, trabalhando como uma class, talvez, 
com todas as funções necessárias, de forma que o usuário seja impedido, assim 
retornará ao ponto que errou para reescrever a quantidade, deste modo o programa não frusturá
quem o usar, quando digitar errado. 
'''
#Importe o tabulate para deixar a tabela mais bonita visualmente.
from tabulate import tabulate
head=["ID","Produto", "Preço","Quantidade"]
#Uma matriz que contém tudo sobre os produtos.
maquina=[[1, "Coca-Cola", 3.75, 2], [2, "Pepsi", 3.67, 5], [3, "Monster", 9.96, 1], [4, "Café", 1.25, 100], [5, "Redbull", 13.99, 2]]

#Uma função que imprime a matriz caso não tenha como acessar o tabulate.
#def produtosMaquina(matriz):
#    for i in matriz:
#        print(i) 

#A função que calcula o troco da quantidade inserida.
def troco(dinheiroColocado, valorProduto):
    troco = dinheiroColocado - valorProduto
    #As notas e moedas que são usadas para calcular o troco.
    notas=[200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    #Se o troco for maior que zero ele ira contar quantas notas e moedas ele deve.
    if troco > 0:
        #Mostra o usuário  seu troco.
        print("Seu troco é:R$", troco)
        for i in range(len(notas)):
            #Variável para definir quantas notas ou moedas ele dara para ousuário .
            quantidadeDeNotas=0
            #Caso o troco seja maior que a nota onde o [i] está, ele ficara sendo diminuido até alcançar zero onde a função termina.
            if troco >= notas[i]:
                #A variável ira gerar o valor das notas e moedas a partir do resultado do troco/notas.
                quantidadeDeNotas=int(troco/notas[i])
                troco -= notas[i]
                #Se o troco for maior que R$1.00 o programa dira que isto é uma nota.
                if troco > 1:
                    print(f"Você ganhara de troco {quantidadeDeNotas} nota(s) de: R${notas[i]}")
                #Se o troco for menor ou igual a R$1.00 o programa dara isso como uma moeda.
                if troco < 1.00 or troco == 1.00:
                    print(f"Você ganhara de troco {quantidadeDeNotas} moedas(s) de: R${notas[i]}")
                #Se o troco for = 0 a função termina.
                if troco == notas[i]:
                    break
    #Se o usuário der a quantidade igual ao valor a maquina não ira dar troco.
    elif troco == 0:
        print("Quantidade perfeita inserida! Não tera troco.")
            
#O programa ira ficar em loop até o úsuario interagir com ele.
while True:
    print(tabulate(maquina, headers=head, tablefmt="fancy_grid"))
    #Para encontrar o ID do produto que o úsuario deseja, eu faço com que ele diminua por 1 por caso que a matriz vai até 4 mas os ID's vão ate 5.
    pedido=int(input("Bem vindo a máquina de vendas! Por favor digite o que deseja: ")) - 1
    #Esse If serve para ver se o pedido for tiver o ID certo(dentro da matriz), ser diferente de 5 por causa do -1 e não ser negativo o programa continua, senão ele pede pra inserir um novo.
    if pedido <= len(maquina) and pedido != 5 and pedido >= 0:
        #Esse If serve para identficar se tem estoque do produto.Se sim o código continua como normal
        #senão o programa fala que não há mais estoque é pede para inserir um novo produto.
        if maquina[pedido][3] > 0:
            print("Você escolheu:", maquina[pedido][1])
            print("Você deve pagar:R$", maquina[pedido][2])
            dinheiro=float(input("Digite o valor que deseja inserir: "))
            #Esse If serve para identificar se o dinheiro inserido pelo o úsuario é o suficiente.Se sim o programa continua como normal
            #senão o programa fala para tentar novamente.
            if dinheiro >= maquina[pedido][2]:
                troco(dinheiro, maquina[pedido][2])
                print("Pagamento feito com sucesso!")
                maquina[pedido][3] -= 1
            else:
                print("O valor colocado é invalido! Tente novamente!")
        else:
            print("O estoque do produto acabou! Digite ela novamente.")
    else:
        print("Valor invalido! Digite novamente.")

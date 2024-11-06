import classes_especializadas_IoT_Monitor as I_Monitor 
from classe_IoT_Lista import IoT_Lista
import funções_banco_de_dados as fun_data

def main():
    for index in range(0, 10):
        l = IoT_Lista('Sistema_IoT_Davi/banco_de_dados_IoT_lista.csv')

        a1 = I_Monitor.Camera(12.4, 'banheiro', 'ligado', 'camera espiã', 'hahaha')
        a2 = I_Monitor.Camera(0.0, 'sala', 'deslogado', 'camera espiã', 'offline')
        b1 = I_Monitor.Janela(35.1, 'cozinha', 'fechada', 'janena de metal', 'online')
        b2 = I_Monitor.Janela(35.1, 'quarto', 'aberta', 'janena de metal', 'offline')

        l.add_item_na_lista("index  local: "+str(index+1))
        l.add_item_na_lista(a1)
        l.add_item_na_lista(a2)
        l.add_item_na_lista(b1)
        l.add_item_na_lista(b2)

        l.salvar_lista()


    l = IoT_Lista('Sistema_IoT_Davi/banco_de_dados_IoT_lista.csv')
    print()
    for itens in l.lista_IoT:
        print(itens)

    print("\n\n\n\n\n\n\n\n\n\n\n")
    for itens in l.dados_IoT_lista:
        print("index global:", l.dados_IoT_lista.index(itens)+1)
        for item in itens:
            print(item)

    print("\n\n\n\n\n\n\n\n")
    fun_data.imprimir_todas_entradas('Sistema_IoT_Davi/banco_de_dados_IoT_lista.csv')

    # print("\nlista geral")
    # print(l.lista_IoT[0])
    # print(l.lista_IoT[1])
    # print(l.lista_IoT[2])
    # print(l.lista_IoT[3])
    # print("\ntipo de cada item da lista")
    # print(type(l.lista_IoT[0]))
    # print(type(l.lista_IoT[1]))
    # print(type(l.lista_IoT[2]))
    # print(type(l.lista_IoT[3]))
    # print("\nlista especializada (de um tipo em especifico)")
    # l.criar_lista_especializada(type(a1))
    # print(l.lista_especializada[0])
    # print(l.lista_especializada[1])
    # print("")



main()

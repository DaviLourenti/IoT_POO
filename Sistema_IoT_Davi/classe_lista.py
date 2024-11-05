import Sistema_IoT_Davi.funções_de_dados as funções_de_dados
import Sistema_IoT_Davi.classes_ItensMonitor as classes_ItensMonitor  

class IoT_Lista:
    def __init__(self, arquivo_csv) -> None:
        self.arquivo_csv = arquivo_csv
        funções_de_dados.verificar_existencia_arquivo(self.arquivo_csv)
        self.dados_IoT_lista = funções_de_dados.ler_todas_entradas(self.arquivo_csv)
        self.lista_IoT = []

        if self.lista_IoT == None:
            self.lista_IoT = []
            print("aoba")

        self.lista_especializada = []
    
    def add_item_na_lista(self, obj_item) -> None:
        self.lista_IoT.append(obj_item)

    def del_item_na_lista(self) -> None:
        del self.lista_IoT[-1]

    def organizar_por_tipos(self):
        pass

    def salvar_lista(self):
        funções_de_dados.adicionar_nova_entrada(self.arquivo_csv, self.lista_IoT)

    def criar_lista_especializada(self, classe_do_item_padrão) -> None:
        for index in range(0, len(self.lista_IoT)):
            if type(self.lista_IoT[index]) == classe_do_item_padrão:
                self.lista_especializada += [self.lista_IoT[index]]




for index in range(0, 100):
    l = IoT_Lista('Sistema_IoT_Davi/dados_IoT_lista.csv')

    a1 = classes_ItensMonitor.CameraMonitor(12.4, 'banheiro', 'ligado', 'camera espiã', 'hahaha')
    a2 = classes_ItensMonitor.CameraMonitor(0.0, 'sala', 'deslogado', 'camera espiã', 'offline')
    b1 = classes_ItensMonitor.JanelaMonitor(35.1, 'cozinha', 'fechada', 'janena de metal', 'online')
    b2 = classes_ItensMonitor.JanelaMonitor(35.1, 'quarto', 'aberta', 'janena de metal', 'offline')

    l.add_item_na_lista("index  local: "+str(index+1))
    l.add_item_na_lista(a1)
    l.add_item_na_lista(a2)
    l.add_item_na_lista(b1)
    l.add_item_na_lista(b2)

    l.salvar_lista()


l = IoT_Lista('Sistema_IoT_Davi/dados_IoT_lista.csv')
print()
for itens in l.lista_IoT:
    print(itens)

print("\n\n\n\n\n\n\n\n\n\n\n")
for itens in l.dados_IoT_lista:
    print("index global:", l.dados_IoT_lista.index(itens)+1)
    for item in itens:
        print(item)


#operaçõesBD.ler_todas_entradas('Sistema_IoT_Davi/dados_IoT_lista.csv')

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
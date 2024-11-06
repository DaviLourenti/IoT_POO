import funções_banco_de_dados as fun_data 

class IoT_Lista:
    def __init__(self, arquivo_csv) -> None:
        self.arquivo_csv = arquivo_csv
        fun_data.verificar_existencia_arquivo(self.arquivo_csv)
        self.dados_IoT_lista = fun_data.ler_todas_entradas(self.arquivo_csv)
        self.lista_IoT = []

        if self.lista_IoT == None:
            self.lista_IoT = []
        self.lista_especializada = []
    

    def add_item_na_lista(self, obj_item) -> None:
        self.lista_IoT.append(obj_item)


    def del_item_na_lista(self) -> None:
        del self.lista_IoT[-1]


    def organizar_por_tipos(self):
        pass


    def salvar_lista(self):
        fun_data.adicionar_nova_entrada(self.arquivo_csv, self.lista_IoT)


    def criar_lista_especializada(self, classe_do_item_padrão) -> None:
        for index in range(0, len(self.lista_IoT)):
            if type(self.lista_IoT[index]) == classe_do_item_padrão:
                self.lista_especializada += [self.lista_IoT[index]]




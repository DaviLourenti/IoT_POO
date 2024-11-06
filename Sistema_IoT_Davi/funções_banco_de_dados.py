import csv
import os


def verificar_existencia_arquivo(arquivo):
    if not os.path.exists(arquivo):
        print("O arquivo não foi encontrado; um será criado para subistitui-lo em sua ausencia")
        try:
            open(arquivo, 'w').close()  
            print("sucesso ao criar o arquivo")
        except:
            print("[ERRO] fracasso ao tentar criar o arquivo")



def adicionar_nova_entrada(arquivo, dados):
    with open(arquivo, mode='a', newline='') as my_arquivo:
        obj_escritor = csv.writer(my_arquivo)
        obj_escritor.writerow(dados) 


def ler_primeira_linha(arquivo):
    with open(arquivo, mode='r') as my_arquivo:
        obj_leitor = csv.reader(my_arquivo)
        linha = next(obj_leitor, None)  

        if linha != [] and linha != None:
            print(linha)  
        else:
            print("O arquivo está vazio.")


def ler_todas_entradas(arquivo):
    lista_obj_lidos = []
    with open(arquivo, mode='r') as my_arquivo:
        obj_leitor = csv.reader(my_arquivo)

        for item_indexado in obj_leitor:
            lista_obj_lidos += [item_indexado] 
        
        return lista_obj_lidos


def imprimir_todas_entradas(arquivo):
    with open(arquivo, mode='r') as my_arquivo:
        obj_leitor = csv.reader(my_arquivo)

        for item_indexado in obj_leitor:
            print(item_indexado)  


def ler_entrada_especifica(arquivo, indice_entrada_especifica=1):
    with open(arquivo, mode='r') as my_arquivo:
        obj_leitor = csv.reader(my_arquivo)
        contador = 0

        for item_indexado in obj_leitor:
            
            contador = contador+1
            if contador == indice_entrada_especifica: 
                print(item_indexado)
                return  
        
        print(f"Entrada com indice {indice_entrada_especifica} não encontrada.")


def ler_ultima_entrada(arquivo):
    with open(arquivo, mode='r') as my_arquivo:
        lista_leitor = list(csv.reader(my_arquivo)) 
        if lista_leitor != []:
            print(lista_leitor[-1])  
        else:
            print("O arquivo está vazio. Pois não há nada na ultima entrada")


def ler_entradas_por_intervalo(arquivo, inicio=1, fim=None):
    with open(arquivo, mode='r') as my_arquivo:
        lista_leitor = list(csv.reader(my_arquivo)) 
        if lista_leitor != []:
            if fim == None:
                fim = len(lista_leitor)

            todas_entradas_do_intevalo = lista_leitor[inicio-1:fim]  
            for entrada in todas_entradas_do_intevalo:
                print(entrada)
        else:
            print("O arquivo está vazio.")


def apagar_linha_especifica(arquivo, numero_linha):
    with open(arquivo, mode='r') as my_arquivo:
        lista_linhas = list(csv.reader(my_arquivo)) 

    if 0 < numero_linha <= len(lista_linhas): 
        del lista_linhas[numero_linha - 1] 
        with open(arquivo, mode='w', newline='') as my_arquivo:
            obj_escritor = csv.writer(my_arquivo)
            obj_escritor.writerows(lista_linhas)  
        print(f"Linha {numero_linha} removida com sucesso.")
    else:
        print("Número da linha inválido.")


def apagar_ultima_linha(arquivo):
        with open(arquivo, mode='r') as my_arquivo:
            lista_linhas = list(csv.reader(my_arquivo)) 

        
        with open(arquivo, mode='w', newline='') as my_arquivo:
            obj_escritor = csv.writer(my_arquivo)
            obj_escritor.writerows(lista_linhas) 

        resposta = input(f"tem certeza? [S-sim/N-não]: {lista_linhas[-1]}")
        if resposta == 'S' or resposta == 's':
            print(f"Linha {lista_linhas[-1]} está sendo removida")
            try:  
                del lista_linhas[-1]  
                print("linha removida com sucesso")
            except:
                print("[ERRO] erro ao tentar apagar a ultima linha")


#arquivo_csv = 'dados_IoT_lista.csv'

# Exemplo de uso
# ler_entrada_especifica(arquivo_csv, 5)
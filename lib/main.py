import flet as ft
from openpyxl import Workbook
from computador import Novo_computador
from tela import pagina
import os

class Main:
    def __init__(self):
        self.computadores = []  # Lista para armazenar os computadores

    def novocomputador(self, setor, usuario, patrimonio, processador, memoria, armazenamento,
                            marca_processador, dispositivo, qualidade, situacao, gpu, placaderede,
                            marca_mouse, tipo_mouse, marca_teclado, tipo_teclado):
        novopc = Novo_computador(setor, usuario, patrimonio, processador, memoria, armazenamento,
                                marca_processador, dispositivo, qualidade, situacao, gpu, placaderede,
                                 marca_mouse, tipo_mouse, marca_teclado, tipo_teclado)
        self.computadores.append(novopc.to_dict())
        print(f"Computador adicionado: {novopc.to_dict()}")  # Mensagem de depuração


    def gera_planilha(self, nome_planilha):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Computadores"
        if not self.computadores:
            print("A lista de computadores está vazia.")
            return None  # Retorna None se a lista estiver vazia
        headers = ["ID"] + list(self.computadores[0].keys())
        sheet.append(headers)
        for idx, computador in enumerate(self.computadores, start=1):
            row = [idx] + list(computador.values())
            sheet.append(row)
        ## Para Testes:  trocar o caminho de armazenamento conforme ambiente executado
        #app_storage_dir = os.path.join("/storage/emulated/0/Download", "MinhasPlanilhas") # Caminho para mobile
        app_storage_dir = os.path.join(os.getcwd(), "MinhasPlanilhasTestes") # Caminho para pc
        os.makedirs(app_storage_dir, exist_ok=True)
        file_path = os.path.join(app_storage_dir, nome_planilha)
        try:
            workbook.save(file_path)
            print(f"Planilha '{file_path}' gerada com sucesso.")
            #self.abrir_planilha(file_path) # Função para testes, abre a planilha
            return file_path  # Retorna o caminho do arquivo
        except Exception as e:
            print(f"Erro ao salvar a planilha: {e}")
            return None

    # Esta funçao é somente para PC -por enquanto-
    def abrir_planilha(self, file_path):
        try:
            os.startfile(file_path)
        except Exception:
            print(f'Erro ao tentar abrir o arquivo {file_path}')

# Código para rodar o aplicativo Flet
if __name__ == "__main__":
    app = Main()
    ft.app(target=lambda page: pagina(page, app))

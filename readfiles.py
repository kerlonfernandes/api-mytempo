from config import *
import os
import re
import os
from datetime import datetime, timezone
from helpers import Helpers

class Intern:
    def __init__(self) -> None:
        self.arquivo_process = ""
    
    def getFileBySession(self, session_file="", type_f=0):
        file_type = None

        if type_f == 0:
            file_type = PATH_REF_DATA
            print(PATH_REF_DATA)
        elif type_f == 1:
            file_type = PATH_BRUTE_DATA
           


        if session_file != "":
            self.arquivo_process = self.searchFileBySession(file_session=session_file, type_f=file_type)
        elif session_file == "":
            self.arquivo_process = self.getMostRecentFileModified(file_type)

            
            return self.arquivo_process

        return None

    

    def processRefinedFile():
        pass

    def getFileSession():
        pass

    def searchFileBySession(self, file_session, type_f=0):
        file_type = ""

        if type_f == 0:
            file_type = PATH_REF_DATA
        elif type_f == 1:
            file_type = PATH_BRUTE_DATA
        else:
            return None
        if file_type and not os.path.exists(file_type):
            return None

        session = f"Sess-{file_session}"
        padrao = re.compile(r"Sess-\d+")
        arquivos = os.listdir(file_type)

        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(file_type, nome_arquivo)
            if padrao.search(nome_arquivo) and session in nome_arquivo:
                return caminho_completo

        return None


    def getMostRecentFileModified(self, diretorio):
        arquivos = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio)]
        if not arquivos:
            return None

        arquivo_mais_recente = max(arquivos, key=os.path.getmtime)
        return arquivo_mais_recente

    def listFiles(self, diretorio):
        try:
            informacoes_arquivos = []
            atletas = set()
            # Lista todos os arquivos no diretório
            arquivos = os.listdir(diretorio)

            for arquivo in arquivos:
                caminho_completo = os.path.join(diretorio, arquivo)
                estatisticas_arquivo = os.stat(caminho_completo)

                with open(caminho_completo) as arq:
                    linhas = arq.readlines()
                    numero_linhas = len(linhas)

                    for linha in linhas:
                        atleta = linha[14:18]
                        atletas.add(atleta)

                informacoes = {
                    'file': arquivo,
                    'path': caminho_completo,
                    'file_size': estatisticas_arquivo.st_size,
                    'last_modify': Helpers.get_file_timestamp_TmzBr(diretorio)['formated_file_timestamp'].strftime(TIME_FORMAT_1),
                    'row_count': numero_linhas,
                    'total_atletas': len(atletas)
                }

                informacoes_arquivos.append(informacoes)

            return informacoes_arquivos

        except FileNotFoundError:
            print(f"O diretório '{diretorio}' não foi encontrado.")
        except PermissionError:
            print(f"Sem permissão para acessar o diretório '{diretorio}'.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def listFilesDiff(self, type_f="refined"):
        files = {}
        if(type_f == "brute"):
            files = self.listFiles(PATH_BRUTE_DATA)
        elif(type_f == "refined"):
            files = self.listFiles(PATH_REF_DATA)
        else:
            return None
        return files


import requests
from config import *
import json
from datetime import datetime
from functions import *

class GetWebData:
    def __init__(self) -> None:
        self.current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def update_equip(self, reader_name, url):
                
        res = {}

        try:
            data_equip = {"nome_equipamento": reader_name}
            # print(data_equip)
            response = requests.post(url=url, json=data_equip)

            if response.status_code == 200:
                updated_data = response.json()
                e = updated_data[0]
                try:
                    with open(READER_CONFIG_FILE_PATH, 'r') as arquivo:
                        dados = json.load(arquivo)
                        
                        dados["data_prova"] = e.get("dataprova")
                        dados["descricao_check"] = e.get("descricao_check")
                        dados["equipamento"] = e.get("equipamento")
                        dados["fabricante"] = e.get("fabricante")
                        dados["hora"] = e.get("hora")
                        dados["idcheck"] = e.get("idcheck")
                        dados["identificacao"] = e.get("identificacao")
                        dados["idprova"] = e.get("idprova")
                        dados["last_update"] = self.current_time
                        dados["modelo"] = e.get("modelo")
                        dados["serie"] = e.get("serie")
                        dados["status"] = e.get("status")
                        dados["tituloprova"] = e.get("tituloprova")

                        with open(READER_CONFIG_FILE_PATH, 'w') as arquivo:
                            json.dump(dados, arquivo, indent=4)
                            arquivo.close()
                        arquivo.close()

                    res['status'] = "success"
                    res['message'] = "Sucesso ao Atualizar Equipamento!"
                    res["erro"] = 0
                    res['retornomsg'] = "Equipamento Atualizado com sucesso!"

                except FileNotFoundError as err:
                    res['status'] = "error"
                    res['message'] = err
                    res["erro"] = 1
                    res['retornomsg'] = "Ocorreu um erro ao Atualizar equipamento!"
                    return res
                # 'status': '',
                # 'message': '',
                # 'erro': 0,
                # 'retornomsg': ''
            else:
                res['status'] = "error"
                res['message'] = "Erro na requisição"
                res["erro"] = 1
                res['retornomsg'] = "Ocorreu um erro na comunicação com equipamento!"
                return res
            
        except Exception as e: 
                res['status'] = "error"
                res['message'] = str(e)
                res["erro"] = 1
                if(IndexError):
                    res['retornomsg'] = "O equipamento não está ativo." 
                else:
                    res['retornomsg'] = "Ocorreu um erro crítico ao Executar esta ação!"
        return res



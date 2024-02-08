from config import *
import requests
from flask import Blueprint, jsonify

import json

class System:

    def __init__(self) -> None:
        pass 
    
    def checkInternet():
        try:
            response = requests.get('https://google.com', timeout=5)
            if response.status_code == 200:
                res = {
                    'status': 'success',
                    'message': 'Conectado à Internet',
                    'erro': 0,
                    'retornomsg': 'O equipamento está conectado á internet'
                }
                return jsonify(res)
            else:
                res = {
                    'status': 'error',
                    'message': 'Sem conexão com a Internet',
                    'erro': 1,
                    'retornomsg': 'O equipamento não está conectado á internet'
                }
                return jsonify(res)
        except requests.ConnectionError:
                res = {
                    'status': 'error',
                    'message': 'Ocorreu um erro na verificação',
                    'erro': 1,
                    'retornomsg': 'O equipamento não está conectado á internet'
                }
                return jsonify(res)

    def getEquipInfo():
        with open(READER_CONFIG_FILE_PATH, 'r') as arquivo:
            equip_data = json.load(arquivo)
            return equip_data

    
    
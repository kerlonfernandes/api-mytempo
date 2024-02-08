from config import *
from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa a extensão CORS
import requests
import json
import time
import subprocess

from system import System
from get_data import GetWebData
from readfiles import Intern
from helpers import Helpers

def start_ngrok(port):
    try:
        
        ngrok_process = subprocess.Popen(['ngrok', 'http', str(port)])

        time.sleep(5)

        response = requests.get('http://127.0.0.1:4040/api/tunnels')
        data = json.loads(response.text)

        public_url = data['tunnels'][0]['public_url']

        return public_url

    except Exception as e:
        print(f"Erro ao iniciar o Ngrok: {e}")
        return None



app = Flask(__name__)
CORS(app)  # Configurações do CORS

@app.route('/')
def obter_ip_exposto():
    # Tenta pegar o endereço IP do cabeçalho X-Forwarded-For
    ip_exposto = request.headers.get('X-Forwarded-For')

    if ip_exposto:
        ip_exposto = ip_exposto.split(',')[0].strip()
    else:
        ip_exposto = request.remote_addr

    return f'O endereço IP exposto é: {ip_exposto}'

@app.route('/status', methods=['GET'])
def status_equip():
    return System.checkInternet();

@app.route('/dados_equipamento', methods=['GET'])
def equip_data():
    return System.getEquipInfo();

@app.route("/atualiza_equipamento", methods=['GET'])
def atualiza_equipamento():
    upd_eqp = GetWebData()
    equip_model = System.getEquipInfo().get("modelo")
    result = upd_eqp.update_equip(equip_model, URL_DADOS_EQUIPAMENTO)

    if result['status'] == 'success':
        return jsonify(result), 200  
    else:
        return jsonify(result), 500

@app.route("/verifica_coleta")
def verificar_coleta():
    pass


@app.route("/buscar_arquivo/bruto/", methods=['POST', 'GET'])
def buscar_arquivo_bruto_last(session=None):
    Files = Intern()
    file_txt = None 
    try:
        file_txt = Files.getFileBySession(type_f=1)


        if file_txt is not None:
            msg = f"Sucesso ao buscar arquivo {file_txt}"
            return jsonify({
                'file_txt': file_txt,
                'status': 'success',
                'message': 'Sucesso ao buscar arquivo',
                'erro': 0,
                'retornomsg': msg,
                'considered_by': 'last_modified'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Não foi possível encontrar o arquivo',
                'erro': 1,
                'retornomsg': 'Arquivo não encontrado.',
                'considered_by': 'last_modified'

            })
    except:
        return jsonify({
            'status': 'error',
            'message': 'Ocorreu um erro crítico',
            'erro': 1,
            'retornomsg': 'Ocorreu um erro ao buscar arquivo.'
        })

@app.route("/buscar_arquivo/bruto/<string:session>", methods=['POST', 'GET'])
def buscar_arquivo_bruto(session):
    Files = Intern()
    file_txt = ""
    try:
        file_txt = Files.searchFileBySession(session, type_f=1)    
        if(file_txt is not None):
            msg = f"Sucesso ao buscar arquivo {file_txt}"
            return jsonify({
                'file_txt': file_txt,
                'status': 'success',
                'message': 'Sucesso ao buscar arquivo',
                'erro': 0,
                'retornomsg': msg,
                'considered_by': 'search_param'
                })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Não foi possível encontrar o arquivo',
                'erro': 1,
                'retornomsg': 'Arquivo não encontrado.',
                'considered_by': 'search_param'

            })
        
    except:
        return jsonify({
            'status': 'error',
            'message': 'Ocorreu um erro crítico',
            'erro': 1,
            'retornomsg': 'Ocorreu um erro ao buscar arquivo.'
        })
    


@app.route("/buscar_arquivo/refinado/", methods=['POST', 'GET'])
def buscar_arquivo_refinado_last():
    Files = Intern()
    file_txt = None 
    try:
        file_txt = Files.getFileBySession(type_f=0)


        if file_txt is not None:
            msg = f"Sucesso ao buscar arquivo {file_txt}"
            return jsonify({
                'file_txt': file_txt,
                'status': 'success',
                'message': 'Sucesso ao buscar arquivo',
                'erro': 0,
                'retornomsg': msg,
                'considered_by': 'last_modified'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Não foi possível encontrar o arquivo',
                'erro': 1,
                'retornomsg': 'Arquivo não encontrado.',
                'considered_by': 'last_modified'

            })
    except:
        return jsonify({
            'status': 'error',
            'message': 'Ocorreu um erro crítico',
            'erro': 1,
            'retornomsg': 'Ocorreu um erro ao buscar arquivo.'
        })



@app.route("/buscar_arquivo/refinado/<string:session>", methods=['POST', 'GET'])
def buscar_arquivo_refinado(session):
    Files = Intern()
    file_txt = ""
    try:
        file_txt = Files.searchFileBySession(session, type_f=0)    
        if(file_txt is not None):
            msg = f"Sucesso ao buscar arquivo {file_txt}"
            return jsonify({
                'file_txt': file_txt,
                'status': 'success',
                'message': 'Sucesso ao buscar arquivo',
                'erro': 0,
                'retornomsg': msg,
                'considered_by': 'search_param'
                })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Não foi possível encontrar o arquivo',
                'erro': 1,
                'retornomsg': 'Arquivo não encontrado.',
                'considered_by': 'search_param'

            })
        
    except:
        return jsonify({
            'status': 'error',
            'message': 'Ocorreu um erro crítico',
            'erro': 1,
            'retornomsg': 'Ocorreu um erro ao buscar arquivo.'
        })

@app.route("/listar_arquivos/brutos/", methods=['POST', 'GET'])
def listar_arquivos_brutos():
    f = Intern() 
    return f.listFilesDiff(type_f="brute")

@app.route("/listar_arquivos/refinados/", methods=['POST', 'GET'])
def listar_arquivos_refinados():
    f = Intern() 
    return f.listFilesDiff(type_f="refined")


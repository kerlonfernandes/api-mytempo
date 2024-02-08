from flask import Flask, request, jsonify
from flask_cors import CORS
from main import app
from functions import w_json
from config import *
import socket


def obter_endereco_ip():
    try:
        # Cria um socket para pegar  host
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print(f"Erro ao obter o endereço IP: {e}")
        return None


if __name__ == '__main__':
    ip_servidor = obter_endereco_ip()
    if ip_servidor:
        data = {
            "server_ip": ip_servidor,
            "port": "5000"
        }
        w_json(f"{PATH_READER_DATA}/server.json", data)
        
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    else:
        print("Não foi possível obter o endereço IP do servidor.")


#         echo "# api-mytempo" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:kerlonfernandes/api-mytempo.git
# git push -u origin main
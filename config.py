import os
import datetime
from datetime import timezone
from datetime import datetime
# CONFIG VARS
now = datetime.now()


#diretorios do sistema

BASE_DIR = os.path.expanduser("~") # /home/USUARIO
APP_NAME = "MyTempo - Cronometragem"
APP_DIR = "/MyTempo"
PATH_READER_DATA = f"{BASE_DIR}{APP_DIR}/Reader_data/"
PATH_BRUTE_DATA = f"{BASE_DIR}{APP_DIR}/Bruto/"
PATH_REF_DATA = f"{BASE_DIR}{APP_DIR}/Refinados/"
READER_CONFIG_FILE_NAME = "equip_data.json"
READER_CONFIG_FILE_PATH = f"{PATH_READER_DATA}{READER_CONFIG_FILE_NAME}" 
MYTEMPO_MYSQL_CONFIG = []
TIME_FORMAT_1 = '%Y-%m-%d %H:%M:%S'
TIME_FORMAT_2 = f"{now.year}{now.month:02}{now.day:02}{now.strftime('%H%M%S%f')[:-3]}" 
# txt_file_name_brute = f'MyTempo-Bruto-Sess-{Helpers.generateRandomNum(4)} T-{TIME_FORMAT_2}.txt'


# APIs

URL_DADOS_EQUIPAMENTO = "http://api.mytempo.esp.br/api/v1/DadosEquipamento.php"
import os
import datetime
from datetime import timezone
import pytz


class Helpers:
    def __init__(self) -> None:
        pass

    def is_num(n):
        if isinstance(n, (int, float)):
            return True
        elif isinstance(n, str) and n.isnumeric():
            return True
        else:
            return False
        
    @staticmethod
    def get_file_timestamp_TmzBr(file_path):

        timestamp = os.path.getmtime(file_path)

        data_utc = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=timezone.utc)

        fuso_horario = pytz.timezone('America/Sao_Paulo')
        data_formatada = data_utc.astimezone(fuso_horario)

        return {'utc_file_timestamp': data_utc, 'formated_file_timestamp': data_formatada}
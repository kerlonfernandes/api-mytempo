from datetime import datetime


now = datetime.now()

formatted_timestamp = f"{now.day:02}/{now.month:02}/{now.year} - {now.strftime('%H:%M:%S.%f')[:-3]}"
# 22/02/2024 - 15:04:34.946
print("Timestamp formatado:", formatted_timestamp)

import requests
import json
import pandas as pd

from datetime import datetime


def check_register_rate():
    api_data = requests.get('https://project-cota-bucket-cota.s3.amazonaws.com/reports/cota_v2_cantidad_registros.json')
    api_data = json.loads(api_data.text)

    datetime_list = []
    devices_list = []

    for item in api_data:
        hora = datetime.strptime(str(list(item.keys())[0]), '%Y-%m-%d %H:%M:%S.%f')
        devices = int(item[list(item.keys())[0]].split(":")[1].strip())

        datetime_list.append(hora)
        devices_list.append(devices)

    df = pd.DataFrame({"Insertion datetime": datetime_list, "Device count": devices_list})

    print(df)


check_register_rate()

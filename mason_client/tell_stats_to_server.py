from typing import *

import requests
from requests import Response
import psutil

import read_config
from Config import Config


def tell()->Union[Dict[str,Any], None]:
    config:Config = read_config.read()
    response:Response = None
    try:
        response = requests.post(
            config.server_uri +"/api/server/submit/0XSADADAWDADFGRsdfesesee",
            headers={"Content-Type":"application/json"},
            json=
                {
                "total_ram": round(psutil.virtual_memory().total / (1024 ** 3), 2),
                "used_ram": round(psutil.virtual_memory().used / (1024 ** 3), 2),
                "cpu_usage":psutil.cpu_percent(interval=1)
                }
        )
        print(response.json())
        return response.json()
    except requests.exceptions.ConnectionError:
        print("server is offline or uri is not correct")
        return

    except requests.exceptions.JSONDecodeError:
        print("given uri returns invalid response")
        print(response.text)
        return

if __name__ == "__main__":
    tell()
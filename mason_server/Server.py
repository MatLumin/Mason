import datetime
from typing import * 

class Server:
    def __init__(self, ip_addrs:str, total_ram:float, used_ram:float, cpu_usage:int):
        self.ip_addrs:str = ip_addrs
        self.total_ram:float = total_ram # in GB
        self.used_ram:float = used_ram #in GB
        self.cpu_usage:int = cpu_usage # in percentage like 85 or 100; a number between 0 and 100
        self.last_contact:datetime.datetime = datetime.datetime.now()

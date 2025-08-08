import time
from typing import * 
import datetime


from telebot import TeleBot

from Server import Server
import is_server_last_contact_too_long_ago
import does_server_has_high_cpu_usage
import does_server_has_high_memory_usage
import generate_report_for_telegram
import send_string_to_targets

def func(servers: Dict[str, Server])->None:
    bot:TeleBot = TeleBot("7597443174:AAEqPcdicppl3A7zsyLZ_0cbKC9i6cZv0Jk")

    while True:
        

        servers_with_lost_connection:List[Server] = []
        servers_with_high_cpu:List[Server] = []
        servers_with_high_ram:List[Server] = []

        ip_addrs:str 
        server:Server
        dont_send_report:bool = False 
        for ip_addrs, server in servers.items():
            dont_send_report = False 

            if is_server_last_contact_too_long_ago.is_it(server) == True:
                servers_with_lost_connection.append(server)

            if does_server_has_high_cpu_usage.does_it(server) == True:
                servers_with_high_cpu.append(server)
                
            if does_server_has_high_memory_usage.does_it(server) == True:
                servers_with_high_ram.append(server)

        no_server_with_lost_connection:bool = len(servers_with_lost_connection) == 0
        no_server_has_high_cpu:bool = len(servers_with_high_cpu) == 0
        no_server_with_high_ram:bool = len(servers_with_high_ram) == 0
        nothing_to_report:bool = no_server_with_lost_connection and no_server_has_high_cpu and no_server_with_high_ram 
        if nothing_to_report == True:
            dont_send_report = True  

        report:str = generate_report_for_telegram.generate(
            servers_with_lost_connection = servers_with_lost_connection,
            servers_with_high_cpu = servers_with_high_cpu,
            servers_with_high_ram = servers_with_high_ram
            )
        if dont_send_report == False:
            send_string_to_targets.send(bot=bot, string=report)
        

        time.sleep(5 * 60) #every 5 minute



if __name__ == "__main__":
    servers:Dict[str, Server] = {}
    servers["A"] = Server("A", 100, 50, 50)
    _15_seconds_ago = datetime.datetime.now() - datetime.timedelta(seconds=15)
    servers["A"].last_contact = datetime.datetime.now()
    #server with high cpu 
    servers["B"] = Server("B", 100, 50, 90)
    #server with high memory 
    servers["C"] = Server("C", 100, 90, 50)

    func(servers=servers)



    

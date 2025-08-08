from typing import * 

from Server import Server 




def generate(servers_with_lost_connection:List[Server] ,servers_with_high_cpu:List[Server] ,servers_with_high_ram:List[Server])->str:
    output = ""


    if servers_with_lost_connection:
        output += "LostConnection⛔:\n"
        for i in servers_with_lost_connection:
            output += "    "+ i.ip_addrs + "\n"
    
    if servers_with_high_cpu.__len__() != 0:
        output += "High Cpu ⚠️:\n"
        for i in servers_with_high_cpu:
            output += "    "+ i.ip_addrs + "\n"

    if servers_with_high_ram.__len__() != 0:
        output += "High Memory Usage ❗:\n"
        for i in servers_with_high_ram:
            output += "    "+ i.ip_addrs + "\n"


    return output



if __name__ == "__main__":
    #test
    print(generate(
        servers_with_lost_connection=[Server("A", 100, 50, 50),Server("A", 100, 50, 50),Server("A", 100, 50, 50)],
        servers_with_high_cpu=[Server("A", 100, 50, 50),Server("A", 100, 50, 50),Server("A", 100, 50, 50)],
        servers_with_high_ram=[Server("A", 100, 50, 50),Server("A", 100, 50, 50)],
    ))

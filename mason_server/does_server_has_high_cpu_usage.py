


from Server import Server 


def does_it(server:Server)->bool:
    ram_percentage:float = server.used_ram/server.total_ram
    return ram_percentage >= 0.85
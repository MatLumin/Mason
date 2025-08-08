

from Server import Server

def does_it(server:Server)->bool:
    return server.cpu_usage >= 85 
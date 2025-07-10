import datetime



class Server:
    def __init__(self, ip_addrs, total_ram, used_ram, cpu_usage):
        self.ip_addrs:Union[None, str] = ip_addrs
        self.total_ram:Union[None, float] = total_ram # in GB
        self.used_ram:Union[None, float] = used_ram #in GB
        self.cpu_usage:Union[None, int] = cpu_usage # in percentage
        self.last_contact:datetime.datetime = datetime.datetime.now()
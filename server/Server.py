



class Server:
    def __init__(self, ip_addrs, total_ram, used_ram, cpu_usage):
        self.ip_addrs:Union[None, str] = ip_addrs
        self.total_ram:Union[None, int] = total_ram # in mbs
        self.used_ram:Union[None, int] = used_ram #in mbs
        self.cpu_usage:Union[None, int] = cpu_usage # in percentage
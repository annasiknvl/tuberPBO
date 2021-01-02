from netmiko import ConnectHandler
 
class konfigR1:
    ##mengkoneksikan router 1 dengan ssh
    def __init__ (self):
        ##login ssh
        self.R1 = {
            'device_type': 'cisco_ios',
            'ip': '192.168.122.2',
            'username': 'admin',
            'password': 'admin'
        }
        ## netmiko mengeksekusi untuk konek ssh ke router
        self.router_connect = ConnectHandler(**self.R1)
        ##netmiko mengeksekusi privilege exec mode
        print(self.router_connect.enable())

    ##mengkonfigurasi ip di router         
    def config_ip(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "interface gig 2/0",
            "ip address 192.168.10.1 255.255.255.0",
            "no shut",
            "exit",
            "interface gig 1/0",
            "ip address 10.10.10.1 255.255.255.252",
            "no shut",
            "exit"
        ]
        ##netmiko mengeksekusi comand
        print(self.router_connect.send_config_set(self.cmd))
    
    ##mengkonfigurasi routing ospf
    def config_osf(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "router ospf 1",
            "network 192.168.10.0 0.0.0.255 area 0",
            "network 10.10.10.0 0.0.0.3 area 0"
        ]
        ##netmiko mengeksekusi comand
        print(self.router_connect.send_config_set(self.cmd))
    
    ##mengkonfigurasi dhcp untuk client
    def config_dhcp(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "ip dhcp pool network 10",
            "network 192.168.10.0 255.255.255.0",
            "default-router 192.168.10.1"
        ]
        ##netmiko mengeksekusi comand
        print(self.router_connect.send_config_set(self.cmd))
        
class konfigR2:
    ##mengkoneksikan router 2 dengan ssh
    def __init__(self):
        self.R2 = {
            'device_type': 'cisco_ios',
            'ip': '192.168.122.3',
            'username': 'admin',
            'password': 'admin'
        }
        self.router_connect = ConnectHandler(**self.R2)
        print(self.router_connect.enable())
    
    ##mengkonfigurasi ip di router
    def config_ip(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "interface gig 2/0",
            "ip address 192.168.20.1 255.255.255.0",
            "no shut",
            "exit",
            "interface gig 1/0",
            "ip address 10.10.10.2 255.255.255.252",
            "no shut",
            "exit"
        ]
        ##netmiko mengeksekusi comand
        print(self.router_connect.send_config_set(self.cmd))
    
    ##mengkonfigurasi routing ospf
    def config_osf(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "router ospf 1",
            "network 192.168.20.0 0.0.0.255 area 0",
            "network 10.10.10.0 0.0.0.3 area 0"
        ]
        print(self.router_connect.send_config_set(self.cmd))

    ##mengkonfigurasi ip dhcp untuk client
    def config_dhcp(self):
        ##comand konfigurasi untuk perangkat cisco
        self.cmd = [
            "ip dhcp pool network 20",
            "network 192.168.20.0 255.255.255.0",
            "default-router 192.168.20.1",
            "exit"
        ]
        print(self.router_connect.send_config_set(self.cmd))
        
    #test koneksi dengan menggunakan ping
    def getPING(self):
        ##comannd untuk ping
        self.cmd = [
            "exit",
            "ping 192.168.10.1",
            "ping 192.168.20.1",
            "ping 10.10.10.1",
            "ping 10.10.10.2"
        ]
        ##netmiko mengeksekusi comand
        print(self.router_connect.send_config_set(self.cmd))
        #netmiko memutuskan koneksi ke router
        self.router_connect.disconnect()


if __name__ == "__main__":
    R1 = konfigR1()
    R1.config_ip()
    R1.config_osf()
    R1.config_dhcp()
    R2 = konfigR2()
    R2.config_ip()
    R2.config_osf()
    R2.config_dhcp()
    R2.getPING()
"""Homework
Extend existing functionality in of app1 class SystemInformation to support

getting available memory (total, used, free)
getting routing table and displaying it as a table"""


import os
import re
class SystemInformation:
    @staticmethod
    def ip_getter():
        result=os.popen('ipconfig')
        for line in result.readlines():
            pattern = "IPv4 Address.*: (?P<IP>.*)"
            match=re.search(pattern,line)
            if match:
                print(match.group("IP"))
    @staticmethod
    def cp_usage():
        result1=os.popen('wmic cpu get loadpercentage')
        for line in result1.readlines():
            pattern = "(?P<cpu_usage>\d+)"
            match1=re.search(pattern,line)
            if match1:
                print(match1.group("cpu_usage"))

    @staticmethod
    def memorie():
        result = os.popen('systeminfo').read()
        pattern = r"(Total Physical Memory:\s+(?P<max_memory>.*))\n(Available Physical Memory:\s+(?P<available_memory>.*))"
        match = re.search(pattern, result)
        if match:
            max_memory = match.group("max_memory")
            available_memory = match.group("available_memory")
            used_memory = str(int(max_memory[:-3].replace(',', '')) - int(available_memory[:-3].replace(',', ''))) + ' MB'
            print("Total Physical Memory: ", max_memory)
            print("Used Physical Memory: ", used_memory)
            print("Available Physical Memory: ", available_memory)
    @staticmethod
    def routing_table():
        tabel_nou = [['Network Destination', 'Netmask', 'Gateway', 'Interface','Metric']]
        result=os.popen('route print').read()
        pattern = r"IPv4 Route Table\n(?P<routing_table>[^\r\n]+((\r|\n|\r\n)[^\r\n]+)*=)"
        match=re.search(pattern,result)
        if match:
            table=match.group("routing_table")
            print(f"IPv4 Route Table este:\n{table}")
            pattern2=r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$'
            for fiecare_rand in match.group("routing_table").splitlines():  # parcurge datele rand cu rand
                linie = list(filter(lambda element: re.fullmatch(pattern2, element), fiecare_rand.split()))  # extrag adrese IP
                if len(linie) == 0:  # elimin lista goala
                    continue
                elif len(linie) == 3:  # linia cu doar 3 IP-uri are 'On-link' la Gateway
                    linie.insert(2, "On-link")
                tabel_nou.append(linie)  # salvam datele in noul tabel
                print(fiecare_rand)
        for i in tabel_nou:
            print(i[0].ljust(25),    i[1].ljust(25),      i[2].ljust(25),      i[3].ljust(25),)


SystemInformation.ip_getter()
SystemInformation.memorie()
SystemInformation.routing_table()
SystemInformation.cp_usage()
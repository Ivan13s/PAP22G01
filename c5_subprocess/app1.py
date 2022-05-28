import subprocess
import re
from time import sleep

class Utils:


    def get_ip_address(self):
        result = subprocess.Popen(['ipconfig'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        for line in stdout.splitlines():
            pattern = 'IPv4 Address.*:(?P<IP>.*)'
            match = re.search(pattern, line)
            if match:
                return match.group("IP")

    def create_new_file(self, file_name):
        result = subprocess.Popen(['notepad', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sleep(3)
        result.communicate(b'Yes')
        result.terminate()

    def get_files(self, path):
        result = subprocess.Popen(['dir', path], shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        return stdout

object = Utils()
# print(object.get_ip_address())
# print(object.create_new_file('fisier'))
print(object.get_files("C:"))
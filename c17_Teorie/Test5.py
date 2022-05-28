# import subprocess
#
#
# result=subprocess.Popen(['ping','8.8.4.4',text=True,stderr=subprocess.PIPE])


#exercitiul 2
# import signal
# import subprocess
# import time
# ping_var=subprocess.Popen(['ping','8.8.4.4'])
# time.sleep(1)
# ping_var.send_signal(signal.CTRL_C_EVENT)
#exercitiul 3
# import subprocess
#
# ping_var=subprocess.Popen(['ping','8.8.4.4'])
# stdout, stderr=ping_var.communicate(timeout=1)

#exercitiul 4
# import subprocess
#
# ping_var=subprocess.Popen(['ping','8.8.4.4'])
# ping_var.terminate()
# print(ping_var.returncode)
#exercitiul 5
# import subprocess
# print(subprocess.run(['dir'],shell=False,text=True,capture_output=True))
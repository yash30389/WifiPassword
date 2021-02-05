import subprocess
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
Profile = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in Profile:
    Password = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
Password = [b.split(":")[1][1:-1]
for b in Password if "key comtent" in b]

try:
    print("{:<30}|  {:<}".format(i,Password[0]))
except IndexError:
    print("{:<30}|  {:<}".format(i,""))
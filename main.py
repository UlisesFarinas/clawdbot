print("CLAWDBOT ONLINE")

import time
import datetime

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"CLAWDBOT HEARTBEAT {now}")
    time.sleep(10)

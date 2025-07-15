import time
import sys 
h=12
m=30
s=0
while True:
    sys.stdout.write(f"\r{h:02}:{m:02}:{s:02}")
    sys.stdout.flush()
    time.sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    if h == 12 and m == 0 and s == 0:
        print("\n12-hour format reached!")
        break

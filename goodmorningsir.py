
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))#not needed
print(timestamp)
timestamp=int( time.strftime('%M'))#not needed
print(timestamp)
timestamp=int(time.strftime('%S'))#not needed
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
name=input("enter your name")
if(timestamp>=18):
    print(f"good night {name}")
elif(timestamp>=16):
    print(f"good evening {name}")
elif(timestamp>=12):
    print(f"good afternoon {name}")
else:
    print(f"good morning {name}")
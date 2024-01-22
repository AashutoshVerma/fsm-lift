import json
import time

for i in range(10):
    with open("params.json", "r") as file:
        data = json.load(file)
        print(data)
    time.sleep(2)
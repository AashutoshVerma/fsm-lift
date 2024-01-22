import json
import time

# Load data from the JSON file
while True :
    with open("params.json", "r") as file:
        data = json.load(file)

    user_input = input("Enter Floor no. or enter 'stop' for Emergency stop: ")

    data['input'] = user_input

    with open("params.json","w") as file:
        json.dump(data, file)
    print("processing...")
    time.sleep(1.5)


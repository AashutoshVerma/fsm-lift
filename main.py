import json
import time

current_floor = 0
building_storey = 10
state = 'idle'
floor_to_stop = []


def temp(i):
    with open("params.json", "r") as file:
        data = json.load(file)
    if data['input'] not in floor_to_stop:
        input_from_outside = data['input']
        if input_from_outside.isdigit():
            floor_to_stop.append(input_from_outside)
        elif input_from_outside.lower() == 'stop':
            print("Stop immediately")
            while input("Enter to key to resume : ") != "key":
                print("Incorrect key")
            clear_outside_input()
    # print(floor_to_stop)
    time.sleep(2)
    print(f"Reached floor no. {i}")
    if str(i) in floor_to_stop:
        print("Stopped at floor : ", i)
        change_state('idle')
        input_at_stop = input("Enter the floor or enter 'c' to close the door : ")
        if input_at_stop not in floor_to_stop:
            if input_at_stop.isdigit():
                print("if")
                floor_to_stop.append(input_at_stop)
                change_state('moving')
            elif input_at_stop.lower() == 'c':
                print("closing the door")
                change_state('idle')
            else:
                print("Enter valid Input")
                floor_to_stop.append(input_at_stop)
        floor_to_stop.remove(str(i))
        clear_outside_input()


def clear_outside_input():
    data = {"input": ""}
    with open("params.json", "w") as file:
        json.dump(data, file)


def change_state(state_change):
    global state
    state = state_change
    print("lift : ", state)


def start_moving(next_floor):
    global current_floor
    global state
    if str(next_floor) not in floor_to_stop:
        floor_to_stop.append(str(next_floor))
    if current_floor < next_floor:
        change_state('moving')
        for i in range(current_floor + 1, next_floor + 1):
            temp(i)
            current_floor = i
    else:
        change_state('moving')
        for i in (reversed(range(next_floor, current_floor))):
            temp(i)
            current_floor = i
    if len(floor_to_stop) != 0:
        next_state(int(max(floor_to_stop)))


def next_state(next_floor):
    global current_floor
    global state
    if next_floor < building_storey:
        if current_floor == next_floor:
            print(f"Already on floor no. {current_floor} ")
        else:
            start_moving(next_floor)
    else:
        print(f"Sorry this floor not available!!")


def main():
    global current_floor
    while True:
        # print("lift : ", state)
        print("Current Floor : ", current_floor)
        next_floor = input("Enter Next floor : ")
        try:
            if next_floor == "exit":
                print("Thanks for using Elevator")
                break
            else:
                next_state(int(next_floor))
        except ValueError:
            print("Enter Valid Floor Number")


if __name__ == "__main__":
    main()

import random
from sys import argv
for filename in argv[1:]:
    with open(filename) as file_obj:
        line = file_obj.readline()
        rows, cols, veh, rides, bonus, step = [int(n) for n in line.split()]
        rides_list = []
        for r in range(rides):
            line = file_obj.readline()
            rides_list.append(list([int(n) for n in line.split()]))
        print(rides_list)
        print()
        print()

        random_rides_list = random.sample(range(0, rides), rides)
        print(random_rides_list)
        rides_per_car = int(rides/veh)

        with open(filename.replace('.in', '.out'), 'w') as output:
            i = 1
            index = 0
            text = ""
            while i <= veh:
                text = str(rides_per_car) + " "
                for r in range(rides_per_car):
                    text += str(random_rides_list[index]) + " "
                    index += 1
                i += 1
                output.write(text)
                output.write("\n")
                print(text)
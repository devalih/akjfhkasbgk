import random
from operator import itemgetter
from sys import argv

rides_list = []


def ridedoable(current_ride, next_ride):
    distance_to_start = abs(current_ride[3] - next_ride[1]) + abs(current_ride[4] - next_ride[2])
    distance_to_finish = abs(next_ride[3] - next_ride[1]) + abs(next_ride[4] - next_ride[2])

    current_time = current_ride[6]
    max_time = next_ride[6]

    if distance_to_finish < next_ride[6] - next_ride[5]:
        return False

    if distance_to_start + current_time <= next_ride[5]:
        return True

    if distance_to_start + distance_to_finish <= max_time:
        return True

    return False


for filename in argv[1:]:
    with open(filename) as file_obj:
        line = file_obj.readline()
        rows, cols, veh, rides, bonus, step = [int(n) for n in line.split()]
        for r in range(rides):
            line = file_obj.readline()
            rides_list.append(list([int(n) for n in line.split()]))
        ii = 0
        for r in rides_list:
            r.insert(0,ii)
            ii+=1
        print(rides_list)

        rides_list = sorted(rides_list, key=itemgetter(6), reverse=True)
        print(rides_list)
        veh_rides = []
        for v in range(veh):
            veh_rides.append([rides_list.pop()])
        ii = 0
        while(rides_list):
            currnt_index = rides_list[-1][0]
            if ii == veh - 1:
                v = 0
            else:
                v = ii+1
            while v != ii:
                if ridedoable(veh_rides[v][-1], rides_list[-1]):
                    veh_rides[v].append(rides_list.pop())
                    ii = v
                    break
                if v  == veh - 1:
                    v = 0
                else:
                    v += 1
            if rides_list and currnt_index == rides_list[-1][0]:
                rides_list.pop()
        print(veh_rides)
        with open(filename.replace('.in', '.out'), 'w') as output:
            for vr in veh_rides:
                output.write(str(len(vr)) + " ")
                for r in vr:
                    output.write(str(r[0]) + " ")
                output.write("\n")
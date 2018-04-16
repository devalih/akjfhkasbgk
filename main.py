import random
from operator import itemgetter
from sys import argv

rides_list = []


def time_to_finish(veh_parm, next_ride):
    distance_to_start = abs(veh_parm[1] - next_ride[1]) + abs(veh_parm[2] - next_ride[2])
    distance_to_finish = abs(next_ride[3] - next_ride[1]) + abs(next_ride[4] - next_ride[2])

    veh_time = veh_parm[0]
    max_time = next_ride[6]

    if distance_to_start + veh_time >= next_ride[5] and veh_time + distance_to_start + distance_to_finish <= max_time:
        return veh_time + distance_to_start + distance_to_finish

    if distance_to_start + veh_time <= next_ride[5]:
        return next_ride[5] + distance_to_finish

    return 0


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
            veh_rides.append([[0,0,0]])
        print(veh_rides)
        ii = 0
        while(rides_list):
            minttf = 99999999
            minveh = 0
            for v in veh_rides:
                ttf = time_to_finish(v[0], rides_list[-1])
                if ttf and ttf <= minttf:
                    minttf = ttf
                    minveh = v
            if minveh:
                minveh[0] = [minttf, rides_list[-1][3], rides_list[-1][4]]
                v.append(rides_list[-1])
            rides_list.pop()
        print(veh_rides)
        with open(filename.replace('.in', '.out'), 'w') as output:
            for vr in veh_rides:
                output.write(str(len(vr)-1) + " ")
                for r in vr[1:]:
                    output.write(str(r[0]) + " ")
                output.write("\n")
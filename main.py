import random
from operator import itemgetter
from sys import argv
for filename in argv[1:]:
    with open(filename) as file_obj:
        line = file_obj.readline()
        rows, cols, veh, rides, bonus, step = [int(n) for n in line.split()]
        rides_list = []
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
            veh_rides[ii].append(rides_list.pop())
            if ii == veh-1:
                ii = 0
            else:
                ii += 1
        print(veh_rides)
        with open(filename.replace('.in', '.out'), 'w') as output:
            for vr in veh_rides:
                output.write(str(len(vr)) + " ")
                for r in vr:
                    output.write(str(r[0]) + " ")
                output.write("\n")
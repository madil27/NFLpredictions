import time
import sys
import random;

path_to_config = "/home/provconf/adil/conf.txt"
path_to_non = "/home/provconf/adil/van.txt"

N = 1000000
config_perc = int(sys.argv[1]);
config_percent = config_perc/100.0


L = list(range(1, N+1))
random.shuffle(L)  # shuffles in-place
# print(L)

config_numbers = config_percent * N;
# print(config_numbers)

f_conf = open(path_to_config,"a")
f_van  = open(path_to_non,"a")
diff = 0
for number in L:
        if(number<=config_numbers):
                start1 = time.time_ns()
                f_conf.write("test-data\n")
                end1 = time.time_ns()
                diff += (end1-start1)
                f_conf.flush()
        else:
                start2 = time.time_ns()
                f_van.write("test-data\n")
                end2 = time.time_ns()
                diff += (end2-start2)
                f_van.flush()
        time.sleep(0.00002)


time_per = diff/N
# print(van_count)
# print(config_count)
print(int(time_per), "ns/op")
f_conf.close()
f_van.close()
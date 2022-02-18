#stroing the runtime of the program in the variable n;
import os
print( os.system("(time -p ./a.out) 2> stats.txt"))
s = str()
with open("stats.txt",'r') as cpu_time:
    s= cpu_time.read()

s = s.replace("\n"," ")
l = s.split()

n = float (float (l[5])+ float(l[3]))

print("the rumtine of the program is : " ,n)

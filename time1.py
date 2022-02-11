import os
os.system("(time ./a.out) 2> stats.txt")
s = str()
with open("stats.txt",'r') as cpu_time:
    s= cpu_time.read()

n = str()
for i in range(0,4):
    n=n+s[i]

k = float(n)
# I have stored the time taken by the program in k
print("the time taken is :" ,k)

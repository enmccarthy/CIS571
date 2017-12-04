path = "/mnt/c/Users/merin/Desktop/CIS571/project/solution.py"
file = open(path, "r")
learn = []
test = []
i = 0
for line in file: 
    x,y = line.split(" ")
    if i%3 == 0:
       test.append((y,x))
    else:
        learn.append((y,x))
    i += 1

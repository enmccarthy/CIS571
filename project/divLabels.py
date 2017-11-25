path = "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/SPAMTrain.label"
file = open(path, "r")
learn = []
test = []
i = 0
for line in file:
    x,y = line.split()
    if i%2 == 0:
       learn.append((x,y))
    else:
        test.append((x,y))
    i += 1

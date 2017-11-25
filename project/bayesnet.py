from __future__ import division
import numpy as np
import os
from divLabels import learn, test
# TODO
#this should probably take the log instead of floating point multi
#becasue the numbers can get too small

# I now need to import test and then run through all of those files
# and test after the bayes net has gone through learn 

#my ugly global variables
trainPositive = {}
trainNegative = {}
negativeTotal = 0
positiveTotal = 0
pA = 0
pNotA = 0

def train():
    global pA, pNotA
    total = 0
    numSpam = 0
    for (label, fileName) in learn:
        if label == 0:
            numSpam +=1
        total += 1
        processEmail(fileName, label)
    pA = numSpam / float(total)
    pNotA = (total - numSpam) / float(total)

def processEmail(fileName, label):
    global trainPositive
    global trainNegative, positiveTotal, negativeTotal
    path = "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/CLEANED_TRAIN"
    fi = open(os.path.join(path, fileName), "r")
    for line in fi:
        for word in line.split():
            if int(label) == 0:
                trainPositive[word] = trainPositive.get(word,0) + 1
                positiveTotal +=1
            else:
                trainNegative[word] = trainNegative.get(word,0) + 1
                negativeTotal +=1

def conditionalWord(word, label):
    global trainPositive
    global trainNegative, positiveTotal, negativeTotal
    if int(label) == 0:
        #print (trainPositive.get(word, 0)+1)/(float)(positiveTotal+(1*positiveTotal + negativeTotal))
        return (trainPositive.get(word, 0)+1)/(float)(positiveTotal+(1*positiveTotal + negativeTotal))
    return (trainNegative.get(word,0)+1)/(float)(negativeTotal+(1*positiveTotal + negativeTotal))

def conditionalEmail(fileName, label):
    result = 1.0
    path = "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/CLEANED_TRAIN"
    fi = open(os.path.join(path, fileName))
    for line in fi:
        for word in line.split():
            result *= conditionalWord(word, label)
    return result

def classify(fileName):
    global pA, pNotA
    isSpam = pA * conditionalEmail(fileName, 0)
    notSpam = pNotA * conditionalEmail(fileName, 1)
    return isSpam > notSpam
                
train()            
totalRight = 0
total = 0
for (label, fileName) in test:
    if classify(fileName) and int(label) == 0:
        totalRight +=1
        total +=1
    elif not classify(fileName) and int(label) == 1:
        totalRight +=1
        total +=1
    else:
        total +=1
print "Total right:"
print totalRight
print "Total files:"
print total
print totalRight/float(total)

from __future__ import division
import numpy as np
import os
import re
from divLabels import learn, test
import codecs
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
    path = "/mnt/c/Users/merin/Desktop/CIS571/project/editedData"
    fi = open(os.path.join(path, fileName), "r")
    for line in fi:
        for word in line.split():
            word = word.lower()
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
    path = "/mnt/c/Users/merin/Desktop/CIS571/project/editedData"
    fi = open(os.path.join(path, fileName))
    for line in fi:
        for word in line.split():
            word = word.lower()
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
print "train negative"
print trainNegative
print "train positive"
print trainPositive
print "top 10 negative"
print sorted(trainNegative, key=trainNegative.get, reverse=True)[:10]
print "top 10 positive"
print sorted(trainPositive, key=trainPositive.get, reverse=True)[:10]

f = codecs.open("positiveWords.txt", "w", "utf-8")
for k, v in trainPositive.iteritems():
    for i in range(v):
         k = re.sub(r'[^\x00-\x7F]',' ', k)
         f.write(k + '\n')
f.close()
f = codecs.open("negativeWords.txt", "w", "utf-8")
for k,v in trainNegative.iteritems():
    for i in range(v):
        k = re.sub(r'[^\x00-\x7F]',' ', k)
        f.write(k + '\n')
        

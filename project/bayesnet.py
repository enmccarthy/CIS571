from __future__ import division
import numpy as np
import os
from divLabels import learn
# TODO
#this should probably take the log instead of floating point multi
#becasue the numbers can get too small
def train:
    total = 0
    numSpam = 0
    for (label, fileName) in learn:
        if label == 0:
            numSpam +=1
        total += 1
        processEmail(fileName, label)
    pA = numSpam/(float)total
    pNotA = (total - numSpam)/(float)total

def processEmail(fileName, label):
    path = "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/CLEANED_TRAIN"
    fi = open(os.join.path(path, fileName), "r")
    for line in fi:
        for word in line.split():
            if label == 0:
                trainPositive[word] = trainPositive.get(word,0) + 1
                positiveTotal +=1
            else:
                trainNegative[word] = trainNegative.get(word,0) + 1
                negativeTotal +=1

def conditionalWord(word, label):
    if label == 0:
        return (trainPositive.get(word, 0)+1)/(float)(positiveTotal+(1*numWords))
    return (trainNegative.get(word,0)+1)/(float)(negativeTotal+(1*numWords))

def conditionalEmail(fileName, label):
    result = 1.0
    path = "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/CLEANED_TRAIN"
    fi = open(os.join.path(path, fileName))
    for line in fi:
        for word in line.split():
            result *= conditionalWord(word, label)
    return result

def classify(fileName):
    isSpam = pA * conditionalEmail(fileName, 0)
    notSpam = pNotA * conditionalEmail(fileName, 1)
    return isSpam > notSpam
                
            
        

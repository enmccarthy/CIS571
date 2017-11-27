import re
import copy
#takes in a sentence represented as an array
removeWords = ["a", "the", "an", "it", "its", "new", "old"]
#eliminate the capital word if it is followed by
followedBy = ["he", "she", "they", "we", "him", "her", "who", "whom"]
#group words that all start with capital
#increase likley hood if it is a 's eliminate following word or group of wordsthough, followed by it
# followed by a word of all caps indicates stock
beginSentence = ["Meanwhile","However,","That", "In", "To","If","Just", "A", "The", "It", "When", "After", "He", "She", "They", "We"]
total = 0

def textElimination(textArr):
    global removeWords, followedBy, total, beginSentence
    #eliminate the word or words (if mulitiple in a row that are capital)
    # that have remove words in front of it
    total += len(textArr)
    textArrCopy = copy.deepcopy(textArr)
    for word in removeWords:
        if word in textArrCopy:
           occur = [i for i, j in enumerate(textArrCopy) if j == word]
           for it in occur:
               if it+1 < len(textArrCopy):
                   while textArrCopy[it+1][0].isupper():
                       textArr.remove(textArrCopy[it+1])
                       it+=1
                       if it+1 >= len(textArrCopy):
                           break
    #print "in between for loops"
    #print textArr
    textArrCopy = copy.deepcopy(textArr)
    currentCapital = False
    previous = False
    for word in textArrCopy:
        if currentCapital:
            if word in followedBy:
                textArr.remove(currentCapital)
            elif previous and word.isupper():
                " ".join(currentCapital, word)
            elif word.isupper():
                currentCapital = word
        else:
            if word.isupper():
                currentCapital = word
    print "before"
    print textArr
    textArrCopy = copy.deepcopy(textArr)
    for word in textArrCopy:
        if not word[0].isupper():
            textArr.remove(word)
        elif word in beginSentence:
            textArr.remove(word)
    return textArr
            
               
file = open("companyArticles.txt", "r")
companyNames = []
for line in file:
    companyNames.append(textElimination(line.split()))
print "Final"
print companyNames
print "total"    
print total

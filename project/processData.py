import errno
import os
import re
from stopWords import stop_words

#TODO
#fix contractions
#delete all one word lines
#delete all lines that have 'var or html etc'
#delete all lines after story body 
def editFiles(dirPath, outPath):
    try:
        os.makedirs(outPath)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(outPath):
            pass
        else:
            raise
    for inputFile in os.listdir(dirPath):
        outputName = inputFile
        file = open(os.path.join(dirPath,inputFile),"r")
        output = open(os.path.join(outPath,outputName), "w+")
        for line in file:
            if not line.strip(): continue
            line = re.sub("\S*\d\S*","",line).strip()
            line = re.sub('[\W_]+', ' ', line, flags=re.UNICODE)
            newLineCopy = line.split()
            newLine = line.split()
            for word in newLineCopy:
               # print word
                if word in stop_words:
                #    print "before"
                #    print newLine
                    newLine.remove(word)
                #    print "after"
                #    print newLine
            joinLine = " ".join(newLine)
            output.write(joinLine + "\n")
        

editFiles("./data/", "./editedData/")

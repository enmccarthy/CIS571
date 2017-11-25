import errno
import os
import re
from stopWords import stop_words
# go through all files in a directory using os.listdir
# remove all non alph characters but keep spaces
#output files to a new directory

#should I remove stop words here (so slow so ugly)
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
        

editFiles("/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING_RESULTS", "/mnt/c/Users/merin/Desktop/CIS571/CSDMC2010_SPAM/CSDMC2010_SPAM/CLEANED_TRAIN")

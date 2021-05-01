# DANIEL MELERAS
# CST 2101: Project 1, text analysis
import re
import os.path

##########################################################################################################
# Classes for program functionality
class TextProcessor:
    """ Class to evaluate text
        Defines static methods that accept lists of strings, ideally lines read from a file object using file.readlines()
        Each method herein returns an appropriate type, e.g methods for counting return integers"""


    @staticmethod
    def countWords(inList):
        tot = 0

        for line in inList: 
            tot += len(line.split())
            
        return tot

    @staticmethod
    def countChars(inList):
        tot = 0

        # count everything except for new line character, and a space
        for line in inList:
            tot += sum(1 for c in line if c not in(' ', '\n'))
       
        return tot

    @staticmethod
    def countSpaces(inList):
        tot = 0
        for line in inList:
            tot += sum(1 for c in line if c==' ')
        return tot

    @staticmethod
    def proportionSpaces(inList):
        totSpaces = 0
        totChars = 0
        
        for line in inList:
            totSpaces += sum(1 for c in line if c==' ')
            totChars += sum(1 for c in line if c not in(' ', '\n'))
        
        return round(100*(totSpaces / totChars), 3)

    @staticmethod
    def wordOccurences(inList):
        """ Counts individual occurences of each word in the text, stores them in a dictionary
            We need to be more careful in parsing the text, to avoid having a double-count of words
            where there is case mismatch"""

        d = {}
        
        for line in inList: 
            line = line.strip()        
            line = line.lower()  # avoid case mismatch 

            words = line.split(" ")
        
            for word in words:
                if word != '':          # don't count empty strings 
                    if word in d:              # check if the word is already in dictionary 
                        d[word] = d[word] + 1  # already there; increment
                    else: 
                        d[word] = 1            # not there; add it with count 1
        
        return d

    @staticmethod
    def wordOccurencesSorted(inList):
        """Does the same as above, except returns the dictionary sorted"""
        d = {}
        
        for line in inList: 
            line = line.strip()        
            line = line.lower()  # avoid case mismatch
             

            words = line.split(" ")
        
            for word in words:
                if word != '':          # don't count empty strings
                    if word in d:              # check if the word is already in dictionary 
                        d[word] = d[word] + 1  # already there; increment
                    else: 
                        d[word] = 1            # not there; add it with count 1

        sortedTuples = sorted(d.items(), key = lambda item: item[1], reverse=True)

        sortedDict = {k: v for k,v in sortedTuples}
        
        return sortedDict    

class FileProcessor:
    """ Gets the input file from the user, and produces the output file"""

    @staticmethod
    def getInput():
        """prompts the user to specify a path for the textfile and stores the file"""

        filePath = input("please specify the file path for the text file you would like analyzed (enter 'exit' to exit):")
        fileName = ''

        # process filename
        if '\\' in filePath:              # user specified windows path
            fileName = filePath.split('\\')[-1].replace('.txt','')
        elif '/' in filePath:             # user specified unix path
            fileName = filePath.split('/')[-1].repalce('.txt','')
        elif 'exit' in filePath:
            print("GoodBye!")
            exit()


        try:
            with open(filePath, mode='r') as f:
                text = f.readlines()

        except FileNotFoundError:
            print("File not found.")
            exit()

        # return tuple of text as list of lines, file name as a string
        return text, fileName

    

    @staticmethod
    def produceOutput(inList, fileName):
        # create file based in fileName
        f = fileName.split('-')[-1]
        
        outFileLocation = Helper.getDocsDirectory()

        outFileName = f'mele0036-PartA-{f}Analysis.txt'
        
        outFile = os.path.join(outFileLocation, outFileName)
        
        # write everything into the file
        try:
            with open(outFile, mode='w') as output:
                output.write("Name of text: " + Helper.getNovelName(f) + '\n')
                output.write("Total Non-Blank Character Count: " + str(TextProcessor.countChars(inList)) + '\n')
                output.write("Total Blank Character Count: " + str(TextProcessor.countSpaces(inList)) + '\n')
                output.write("Percentage Blank Characters: " + str(TextProcessor.proportionSpaces(inList)) + '%\n')
                output.write("Total Word Count: " + str(TextProcessor.countWords(inList)) + '\n')
                output.write("Word, count: " + '\n')
                for k, v in TextProcessor.wordOccurencesSorted(inList).items():
                    output.write(f'  {k}: {v}\n')
        except IOError:
            print("Directory not found")

class Helper:
    """Helper methods for the other classes"""

    @staticmethod
    def getNovelName(inStr):
        l = [a for a in re.split(r'([A-Z][a-z]*)', inStr) if a]
        novel = ""
        for part in l:
            if part != "Clean" and part != "Removed": # for the purposes of this project only
                novel += part + " "
        return novel

    @staticmethod
    def getDocsDirectory():
        home = os.path.expanduser('~')

        docs = os.path.join(home, 'Documents')

        return docs




##########################################################################################################
# Main guard in case classes are being imported
def main():
    fileTup = FileProcessor.getInput()

    FileProcessor.produceOutput(fileTup[0], fileTup[1])

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:21:39 2018

@author: William Keilsohn
"""

# Import the nltk books and create a list of them

from nltk.book import *
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize

bookLis = [text1, text2, text3, text4, text5, text6, text7, text8, text9]

#Determine the use of "However" via the concordence tool for the discussed texts
## First define a useful helper function

def howeverFinder(text):
    '''
    #Here was my original solution/code before the blackboard assinment was changed
    howevs = text.concordance_list('however', lines=960900) #http://www.nltk.org/_modules/nltk/text.html
    #Turns out the concordance function normally has a limit of 25.
    #https://stackoverflow.com/questions/41135369/get-all-results-frm-nltk-concordance
    #https://themillions.com/2007/09/world-longest-novel.html
    #Special thanks to the Anon(s) on Piazza that pointed this solution out!    
    totalHowevers = len(howevs) #Determines how many times however is used in the text.
    startHowevers = 0
    middleHowevers = 0
    howeverConclusions = ""
    for i in howevs: # Goes through the text an counts the number of "however"'s present.
        if i[0][-1] == ".": #Looks to see if the last token before the however is a period or a comma. // https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
            startHowevers += 1
        elif i[0][-1] == '"': #Some times the sentence ends in quotations // https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
            startHowevers += 1
        else:
            middleHowevers += 1 #These will probably be commas but not always.
            '''
    '''
    #Another possible solution:
    #They accuracy between the two in debatable. For text6 this one is clearly better, but for text1 the above is probably more accurate. 
    #Unfortunitly it's a matter of grammar rules.
    #https://www.scribendi.com/advice/capitalization.en.html
    startHowevers = text.count('However') #http://sapir.psych.wisc.edu/programming_for_psychologists/cheat_sheets/Text-Analysis-with-NLTK-Cheatsheet.pdf
    middleHowevers = text.count('however') #http://sapir.psych.wisc.edu/programming_for_psychologists/cheat_sheets/Text-Analysis-with-NLTK-Cheatsheet.pdf
    totalHowevers = startHowevers + middleHowevers
    howeverConclusions = ""
    '''
    ###This next section is the new code
    startHowevers = 0
    middleHowevers = 0
    howeverConclusions = ""
    totalHowevers = 0
    bookHolderLis = text[0:]
    bookHolderStr = ' '.join(bookHolderLis)#https://stackoverflow.com/questions/44105617/convert-a-list-to-string-in-python
    bookHolderSent = sent_tokenize(bookHolderStr)
    for x in bookHolderSent:
        bookHolder = word_tokenize(x)
        if 'however' in bookHolder:
            middleHowevers += 1
        elif "However" in bookHolder: #In favor of text6, and w/o a good way to check every instance, I'm going to use the capitalization based method. 
            startHowevers += 1 #In a perfect world one could tell a new speech blurb from a new clause, but unfortunitly gramar isn't that straight forward.
            #https://www.scribendi.com/advice/capitalization.en.html
    totalHowevers = startHowevers + middleHowevers
    ### End of new code
    if startHowevers > middleHowevers:
        howeverConclusions = """The author appears to prefer the 'in whatever way/to whatever extent' usage of the word. 
        This would imply that the sentence in question is closely related to the preceding one. Without reading the text
        not much else can be determined.\n"""
        #https://web.sonoma.edu/users/f/farahman/subpages/utilities/however.pdf
        #https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
    elif middleHowevers > startHowevers:
        howeverConclusions = """The author appears to prefer the 'nevertheless' useage of the word.
        This would imply that the sentence in question is a conjunction of two clauses which could stand alone, and/or 
        the author wishes to emphasize a specific point as being in contrast to an earlier one. Without reading the actual text it 
        is difficult to determine.\n"""
        #https://web.sonoma.edu/users/f/farahman/subpages/utilities/however.pdf
        #https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
    elif totalHowevers == 0:
        howeverConclusions = """The author never uses the word 'however'.
        Therefore, no useful information is offered.\n"""
        #https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
    else:
        howeverConclusions = """ The author appears to have no preference for either form of the word 'however'.
        As a result, no useful information can be obtained. \n"""
        #https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
    howeverResults = [totalHowevers, startHowevers, middleHowevers, howeverConclusions] #having a list will be easier to call later.
    return howeverResults

##Now to create a file to write to an loop through the texts
    
from nltk.corpus import gutenberg #https://www.nltk.org/book/ch02.html
booksGuten = gutenberg.fileids()  #https://www.nltk.org/book/ch02.html

#bookFile = open("bookfile.txt", "w") #Generates a new file.

def countHowever(lis, filePath): #Function to produce a file with run down of all the howevers found in the list of "books".
    file = open(filePath, "w")
    file.write("This is a summary of the number of 'Howevers' present in the selected texts. \n")
    file.write("\n") #I like to skip a line to make things look pretty.
    for i in lis:
        file.write(str(i.name) + ": ")#Turns out you can just call the name as a component. Coudln't find it online anywhere, so I just fooled around in the consoul.
        file.write("Total 'Howevers': ")
        file.write(str(howeverFinder(i)[0]))
        file.write("; Of these, there is/are ")
        file.write(str(howeverFinder(i)[1]))
        file.write(" which sart(s) a sententance and ")
        file.write(str(howeverFinder(i)[2]))
        file.write(" which can be found in the middle of a sentence. \n")
        file.write(howeverFinder(i)[3])
        file.write("\n") #Looks a little nicer with some extra space.
    file.close()
        
countHowever(bookLis, "bookfile.txt") #Produces file and answers question question.
#bookFile.close()
    

# Do this for the Gutenberg texts
##First I need to get the Gutenberg books/texts and store them in a list. 
'''
Moved these up b/c python reads down a file.
from nltk.corpus import gutenberg #https://www.nltk.org/book/ch02.html
booksGuten = gutenberg.fileids()  #https://www.nltk.org/book/ch02.html
'''

## Have to make "books" into "books" that python can read.

import nltk.corpus #https://stackoverflow.com/questions/29110950/python-concordance-command-in-nltk
from nltk.text import Text #https://stackoverflow.com/questions/29110950/python-concordance-command-in-nltk

def bookWriter(lis):
    actualBook = "Blank space, baby!" #Please be a T-swift fan. 
    bookLis = []
    for i in lis:
        actualBook = Text(nltk.corpus.gutenberg.words(i)) #https://stackoverflow.com/questions/29110950/python-concordance-command-in-nltk
        bookLis.append(actualBook) #It's best to just add them to the end, rather than replacing.
    return bookLis

bookLis2 = bookWriter(booksGuten)    
##Now I need to loop through them an write my information to the text file. 

countHowever(bookLis2, "gutenfile.txt") #Answers question. 

# Obtain a Brown Corpus category: https://www.nltk.org/book/ch02.html

from nltk.corpus import brown


'''
Convert Corpus into a text file:
https://gist.github.com/JonathanReeve/ac543e9541d1647c1c3b
Please assume the above reference for the majority of the following function.
A large portion of the function is from the link.
'''
def corpConvert(cat): #https://gist.github.com/JonathanReeve/ac543e9541d1647c1c3b
    wordLis = brown.words(categories = cat) #Generates a list of the words in the category
    wordPure = " ".join(wordLis) #Turns the above list into a single string of words
    fileName = cat + '.txt' #Because the name of each category is a string it can be passed in as such.
    BrownFile = open(fileName, "w") #One has to create the actual text file
    BrownFile.write(wordPure)
    BrownFile.close()
    return fileName #https://stackoverflow.com/questions/11676458/how-do-i-name-a-file-by-a-variable-name-in-python

'''
End major citation.
Returing to normal inline commenting.
'''
# Now I should make a list of named files

brownLis = [corpConvert('news')]    


# Turns out Gutenberg files and regular txt files require different functions for conversion.

def bookWriter2(lis):
    actualBook = ""
    bookLis = []
    fileName = ""
    for i in lis:
        textBook = open(i, "r") #https://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes
        allText = textBook.read() #https://stackoverflow.com/questions/10467024/how-do-i-create-my-own-nltk-text-from-a-text-file
        words = nltk.word_tokenize(allText)#https://stackoverflow.com/questions/10467024/how-do-i-create-my-own-nltk-text-from-a-text-file
        fileName = i.strip('.txt')#https://www.techwalla.com/articles/how-to-insert-the-date-and-time-in-a-website
        actualBook = nltk.Text(words, name = fileName)#https://stackoverflow.com/questions/10467024/how-do-i-create-my-own-nltk-text-from-a-text-file
        #https://www.programcreek.com/python/example/81634/nltk.Text
        bookLis.append(actualBook)
    return bookLis
'''
brownLis2 = bookWriter2(brownLis)
countHowever(brownLis2, "news.txt") #Answers the question.
Moved this to after the bonus b/c the bonus deletes this file. 
'''
  
# Bonus: Loop through the entier Brown corpus and write a doc(s) for them.

import os #https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/

'''
Origninally I had a note here stating that this last part made the program run slow.
However since I re-worked it to include the new fucntion we were given, the whole thing just seems to be slow.
Additionally, concordance thinks there are always a few more instances of the word per text (except when there are none)than this new method.
I have no idea though how to find those extras and/or if they actually are extra. 
All I want to say here is that you have been warned regarding the speed of this program. 
'''


def bookLooper(lis):
    textBookLis = []
    textBook = ""
    for i in lis:
        textBook = corpConvert(i)
        textBookLis.append(textBook)
    textBookWritten = bookWriter2(textBookLis)
    countHowever(textBookWritten, "brownreport.txt")
    for x in textBookLis: #https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
        os.remove(x)
        
bookLooper(brown.categories()) #Answers the Question

### Due to the remove function, the file needs to be re-written. 
newsText = open("news.txt.", "w") #Re-creates the file in question to prevent an error
newsText.close() #Generally a bad idea just to leave a file open.

brownLis2 = bookWriter2(brownLis)
countHowever(brownLis2, "news.txt") #Answers the question.        
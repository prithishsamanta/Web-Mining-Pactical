# Reading Sentence from a file
print("Reading SENTENCE")
print(' \n ')
f=open( "./temp1.txt" )
sen = f.read()
print(sen)
f.close()
print( '\n' )

# Reading Paragraph from a file
print("Reading PARAGRAPH")
print(' \n ')
f = open( "./temp2.txt" )
para = f.read()
print(para)
f.close()
print( '\n' )

#Removing PUNCTUATIONS
import nltk
nltk.download('punkt')
import re
sen2 = re.sub( r'[^\w\s]' , '' ,sen)
para2 =re.sub( r'[^\w\s]' , '' ,para)
print(sen2)
print('\n')
print(para2)
print('\n')

from nltk.tokenize import word_tokenize
tokensen = word_tokenize(sen2)
tokenpara = word_tokenize(para2)
print(tokensen)
print( '\n' )
print(tokenpara)
print( '\n' )

#Removing Stop Words
print("Removing STOPWORDS")
print(' \n ')
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words( 'english' )
print(stopwords)

stopsen = []
for m in tokensen:
    if(not m in stopwords):
        stopsen.append(m)

stoppara = []
for n in tokenpara:
    if(not n in stopwords):
        stoppara.append(n)
        
print(stopsen)
print( '\n' )
print(stoppara)
print( '\n' )

#Stemming using nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemsen = []
stempara =[]
print("Performing STEMMING")
print(' \n ')
for word_nltk1 in stopsen:
    stemsen.append(stemmer.stem(word_nltk1))
for word_nltk2 in stoppara:
    stempara.append(stemmer.stem(word_nltk2))
print(stemsen)
print( '\n' )
print(stempara)
print( '\n' )

#Finding the Frequency
from collections import Counter
fsen = Counter(stemsen)
fpara = Counter(stempara)
print("Calculating FREQUENCY")
print('\n')
print( "Initial sentence: " +sen)
print('\n')
print('Final sentence: \n')
print(fsen)
print('\n')
print("Initial paragraph: " +para)
print('\n')
print('Final paragraph : \n')
print(fpara)
print('\n')

#Same for a webpage
#Reading Content from the webpage
import urllib.request
import urllib.parse
import re
url='http://www.doc.ic.ac.uk/~susan/121/tut4.pdf'
req = urllib.request. Request(url)
resp = urllib.request.urlopen(url)
webpage = resp.read()
print('Webpage response' , webpage)
webpara = re.findall( r'<p>(.*?)</p>' ,str(webpage))
web_string = ''
for para in webpara:
     web_string = web_string + para
print('web_string',web_string)

#Removing PUNCTUATIONS
import nltk
nltk.download('punkt')
import re
webparapunc =re.sub( r'[^\w\s]' , '' ,web_string)
print(webparapunc)

from nltk.tokenize import word_tokenize
tokenweb = word_tokenize(webparapunc)
print(tokenweb)

#Removing Stop Words
print("Removing STOPWORDS")
print('\n')
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = stopwords.words( 'english' )
print(stopwords)

stopwordweb = []
for p in tokenweb:
    if not p in stopwords:
        stopwordweb.append(p)
print(stopwordweb)

#Stemming using nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemweb = []
print("Performing STEMMING")
print(' \n ')
for word_nltk3 in stopwordweb:
    stemweb.append(stemmer.stem(word_nltk3))
print(stemweb)

#Finding the Frequency
from collections import Counter
fweb = Counter(stemweb)
print("Calculating FREQUENCY")
print('\n')
print("Initial Webpage: " +web_string)
print('\n')
print('Final Webpage : \n')
print(fweb)

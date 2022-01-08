import PyPDF2

print("Reading SENTENCE")
file = open("./Mid Term.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
page1 = reader.getPage(0)
data = page1.extractText()


# Reading Sentence from a file taken from link http://www.doc.ic.ac.uk/~susan/121/tut4.pdf
print("Reading SENTENCE")
sen = ""
for m in data:
    if m == ".":
        break
    else:
        sen = sen + m
    
print(sen)
print()

# Reading Multiple Sentence from a file taken from link http://www.doc.ic.ac.uk/~susan/121/tut4.pdf
print("Reading MULTIPLE SENTENCES")
m_sen = ""
i = 0;
for m in data:
    if i == 2:
        break
    elif m == "." and i < 2:
        i=i+1
        m_sen = m_sen + m
    else:
        m_sen = m_sen + m

print(m_sen)
print()

# Reading Paragraph from a file taken from link http://www.doc.ic.ac.uk/~susan/121/tut4.pdf
print("Reading PARAGRAPH")
para = ""
i = 1;
for m in data:
    if i == 5:
        break
    elif m == "." and i < 5:
        i=i+1
        para = para + m
    else:
        para = para + m

print(para)
print()

#Removing PUNCTUATIONS
import nltk
nltk.download('punkt')
import re
sen2 = re.sub( r'[^\w\s]' , '' ,sen)
m_sen2 = re.sub( r'[^\w\s]' , '' ,m_sen)
para2 =re.sub( r'[^\w\s]' , '' ,para)


from nltk.tokenize import word_tokenize
tokensen = word_tokenize(sen2)
tokenm_sen = word_tokenize(m_sen2)
tokenpara = word_tokenize(para2)
print("Tokenizing Sentence")
print(tokensen)
print( '\n' )
print("Tokenizing Mutliple Sentences")
print(tokenm_sen)
print( '\n' )
print("Tokenizing Paragraph")
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

stopm_sen = []
for k in tokenm_sen:
    if(not k in stopwords):
        stopm_sen.append(k)

stoppara = []
for n in tokenpara:
    if(not n in stopwords):
        stoppara.append(n)

#Stemming using nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemsen = []
stemm_sen = []
stempara =[]
print("Performing STEMMING")
print(' \n ')
for word_nltk1 in stopsen:
    stemsen.append(stemmer.stem(word_nltk1))
for word_nltk2 in stopm_sen:
    stemm_sen.append(stemmer.stem(word_nltk2))
for word_nltk3 in stoppara:
    stempara.append(stemmer.stem(word_nltk3))
print(stemsen)
print( '\n' )
print(stemm_sen)
print( '\n' )
print(stempara)
print( '\n' )

#Finding the Frequency
from collections import Counter
fsen = Counter(stemsen)
fm_sen = Counter(stemm_sen)
fpara = Counter(stempara)
print("Calculating FREQUENCY")
print('\n')
print( "Initial Sentence: " +sen)
print('\n')
print('Final Sentence: \n')
print(fsen)
print('\n')
print( "Initial Multiple Sentence: " +m_sen)
print('\n')
print('Final Multiple Sentence: \n')
print(fm_sen)
print('\n')
print("Initial Saragraph: " +para)
print('\n')
print('Final Paragraph : \n')
print(fpara)
print('\n')

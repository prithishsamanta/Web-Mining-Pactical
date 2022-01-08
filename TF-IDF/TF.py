import glob
import math
import nltk
from nltk.corpus import stopwords
line=''
s=set()
flist=glob.glob(r'C:\Users\Prithish\Desktop\studies\Web mining\Lab\TFIDF\*.txt') #get all the files from the d`#openeach file >> tokenize the content >> and store it in a set
print("list of files are \n", flist)
for fname in flist:
    tfile=open(fname,"r")
    line=tfile.read() # read the content of file and store in "line"
    tfile.close() # close the file
    s=s.union(set(line.split(' '))) # union of common words

withoutStopwords = []
stopwords = stopwords.words('english')
 
for i in s:
    if (i not in stopwords):
        withoutStopwords.append(i)
    else:
        print('stopWord removed:' + i + '\n')
 
s=sorted(withoutStopwords) # sorts the content alphabetically
print("List of words\n",s)
 
final_line='TERM'+'\t'
i=1
for f in flist:
    final_line+='D'+str(i)+' '+'\t'
    i+=1
final_line+='\n'
 
for term in s:
    final_line+=(term + '\t')
    for fdoc in flist:
        doc=open(fdoc)
        line=doc.read()
        doc.close()
        final_line+=str(line.count(str(term)))+'\t'
    final_line+='\n'

print(final_line)

print("\n\nWriting the contents into the 4th file...\n")
f = open("doc4.txt", "w")
for i in s:
    f.write(str(i) + ', ')
f.close()
print("Written into the file!\n")

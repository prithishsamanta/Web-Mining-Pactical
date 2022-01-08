import glob
import math
import nltk
from nltk.corpus import stopwords
line=''
s=set()
flist=glob.glob(r'C:\Users\Prithish\Desktop\studies\MICRO ECO\Lab\TF-IDF\TFIDF') #get all the files from the d`#openeach file >> tokenize the content >> and store it in a set
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
 
i=0
ct=0
tf_line=''
doc_counts=[]
for term in s: #takes each term in the set
    doc_counts.append(0)
    for fdoc in flist: # counts the no of times "term" is encountered in each doc
        doc=open(fdoc)
        line=doc.read()
        doc.close()
        ct=line.count(str(term)) #counts the no. of times "term" is present in the file
        tf_line+=str(ct)+',' #prints the count in each doc seperated by comma
        if (ct>0): #counts no of docs in which
            doc_counts[i]+=1 #this "term" is found
    i+=1
    tf_line=tf_line.strip()+'\n'
 
idf=[] #inverse document frequency
weights=[] #weight
total_docs=len(flist) #total number of documents
 
i=0
for doc_count in doc_counts: #takes the 1st doc count
    idf.append(math.log(total_docs/doc_count)) #calculates idf for each "term"
    weights.append(idf[i]*doc_count) #calculate weight of the term
    i+=1
 
final_line='TERM'+'\t'
i=1
for f in flist:
    final_line+='D'+str(i)+' '+'\t'
    i+=1
final_line+='\t'+'IDF'+'\t'+'TF-IDF\n'
tf_arr=tf_line.split('\n')
 
i=0
for term in s:
    final_line+=term+'\t'+tf_arr[i]+'\t'+str(round(idf[i],2))+'\t'+' '+str(round(weights[i],2))+'\t'+'\n'
    i+=1
 
print(final_line)

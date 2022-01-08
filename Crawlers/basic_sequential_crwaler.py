#the code fetches the url by putting a request
#beautifulsoup is a python library used to extract data from html
#impoting stopwords using nltk
#we then assign the url to the root url variable
#reponse.read() is used to read the content and store it in a variable
#soup.prettify() is used to format the html format
#soup.find_all('a', href=True) helps us to find all the anchor tags present and stores it in a list
#urljoin() is used to join root url variable and the url variable, joins base url with relative url
#after extracting the urls from the webpage it removes the stopwords from it and prints the frequency of the words


from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import nltk
from nltk.corpus import stopwords
response = urllib.request.urlopen('https://www.apple.com/in/')
root_url = 'http://php.net/'
html = response.read()
print('HTML \n', html)
soup = BeautifulSoup(html, 'html5lib')
print('\n FORMATTED HTML: \n', soup.prettify())
text = soup.get_text(strip='true')
print('TEXTUAL \n', text)
links = soup.find_all('a', href=True)
print('\n LINKS \n', links)
outlinks = []
for link in links:
    print('loop starts', link)
    url = link['href']
    print('URL \n', url)
    if url.startswith(root_url):
        url = urljoin(root_url, url)
        print('URL after join \n', url)
        outlinks.insert(1, url)
print('TEXT AND LINKS \n')
print('OUTLINKS local urls \n', outlinks)
 
tokens = [t for t in text.split()]
print('TOKENS \n', tokens)
print('NUMBER OF TOKENS \n',len(tokens))
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
print('TOKENS AFTER STOP WORD REMOVAL \n', clean_tokens)
print(len(clean_tokens))
print('NUMBER OF STOPWORDS \n', len(tokens) - len(clean_tokens))
freq = nltk.FreqDist(clean_tokens)
print('\n FREQ', freq, '\n')
print(freq.items())
for key, val in freq.items():
    print(str(key) + ' : ' + str(val))

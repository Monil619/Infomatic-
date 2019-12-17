#importing Library
import urllib
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.tokenize import RegexpTokenizer

#loding webiste url
main_url= "https://www.nbcnews.com"

#storing html variables in main
main= urllib.request.urlopen(main_url)

#making the soup load
soup = BeautifulSoup(main, "lxml")

#creating list to load all headlines
finding_headline=[]

#looping to find headline
for i in soup.find_all(class_="headline___38PFH"):
    story_title = i.text.replace("\n", " ").strip()
    new_story_title1 = str(story_title.encode('utf-8'))
    new_story_title=str(new_story_title1)[2:-1]
    new_list = new_story_title.split()

    #printing headline before claening
    print(new_story_title)

    for w in new_list:
        if w.isalpha():
            finding_headline.append(w)

#Removing numerial data
num = []

for i in finding_headline:
    if i.isdigit() == False:
        num.append(i)

#creating list of stop words
stop = []
with open('stopwords_en.txt', 'r') as file:
    filecontents = file.readlines()
    for line in filecontents:
        word = line[:-1]
        stop.append(word)

#Performed to check most frequent words in list
wordfreq = []
for w in num:
    wordfreq.append(num.count(w))

# map frequency to each word
map_freq = zip (num, wordfreq)
map_freq = set(map_freq)
map_freq = list(map_freq)

# sort frequencies according to frequency
sorted_freq = sorted(map_freq, key=lambda x: x[1])

# retrieve all frequently used words
freq = sorted_freq[:]

#finished checking frequently used words and further adding them in stopword list to remove them all

#Adding words stopwords list which are most frequently occured so that its easy to remove them
stop.append('in')
stop.append('of')
stop.append('and')
stop.append('the')

#Removing stopwords
new_words = []

for i in num:
    if i not in stop:
        new_words.append(i)

#printing headline after cleaning
print("\nprinting headline after cleaning\n")
print(new_words)

# joining list to perform wordcloud analysis
sent=""
sent=' '.join(new_words)
#print(sent)

#extracting bigrams
Bigrams=[]
replace=[]
bigram=list(nltk.bigrams(new_words))
for i in bigram:
    Bigrams.append(i)
replace=['_'.join(map(str, x)) for x in Bigrams]

#counting bigrams
wordfre = []
for w in replace:
    wordfre.append(replace.count(w))

#map frequency to each word
map_fre = zip (replace, wordfre)
map_fre = set(map_fre)
map_fre = list(map_fre)

# sort frequencies according to frequency
sorted_fre = sorted(map_fre, key=lambda x: x[1])

# retrieve maximum occuring words
fre = sorted_fre[:]

#adding bigrams in clean list
# for i in fre:
#     new_words.append(i)

# print(new_words)

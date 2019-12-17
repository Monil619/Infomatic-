import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import sentiwordnet as swn

# Using regular expressions form nltk
tokenizer = RegexpTokenizer(r'\w+')

# Importing the pros, cons and stopwords file.
data_pro = open("pro_ marijuana_raw.txt")
data_con = open("con_ marijuana_raw.txt")

# Removing Lower case, blank lines and space
pro = data_pro.read().lower().replace("\n", " ")
con = data_con.read().lower().replace("\n", " ")

#creating list of stop words
stop = []
with open('stopwords_en.txt', 'r') as file:
    filecontents = file.readlines()
    for line in filecontents:
        word = line[:-1]
        stop.append(word)

#Remove Punctuation using tockenizer
pro = tokenizer.tokenize(pro)
con = tokenizer.tokenize(con)

#Removing numerial data( point 2 , removing unnecessary data as to undestand sentiments there is no need of numeric values)
num_pro = []
num_con = []

for i in pro:
    if i.isdigit() == False:
        num_pro.append(i)

for i in con:
    if i.isdigit() == False:
        num_con.append(i)

##Performed to check most frequent words in both list

# Counting Frequently used words
#wordfreq_con = []
#for w in num_con:
#    wordfreq_con.append(num_con.count(w))

#wordfreq_pro = []
#for w in num_pro:
#    wordfreq_pro.append(num_pro.count(w))

## map frequency to each word
#map_freq_con = zip (numcon, wordfreq_con)
#map_freq_con = set(num_con)
#map_freq_con = list(num_con)

#map_freq_pro = zip (num_pro, wordfreq_pro)
#map_freq_pro = set(num_pro)
#map_freq_pro = list(num_pro)

## sort frequencies according to frequency
#sorted_freq_con = sorted(map_freq_con, key=lambda x: x[1])
#sorted_freq_pro = sorted(map_freq_pro, key=lambda x: x[1])

#print(sorted_freq_con)
#print(sorted_freq_pro)
##finished checking frequently used words and further adding them in stopword list to remove them all

#Adding words stopwords list which are most frequently occured so that its easy to remove them
stop.append('Marijuana')
stop.append('marijuana')
stop.append('drug')
stop.append('legal')
stop.append('use')
stop.append('cannabis')
stop.append('legalization')
stop.append('people')
stop.append('billion')
stop.append('states')

#Removing stopwords
new_words_pro = []
new_words_con = []

for i in num_pro:
    if i not in stop:
        new_words_pro.append(i)

for i in num_con:
    if i not in stop:
        new_words_con.append(i)

## joining list to perform sentiment analysis
sent_con=""
sent_con=' '.join(new_words_con)

sent_pro=""
sent_pro=' '.join(new_words_pro)

## printing to test word clouds
#print(sent_con)
#print(sent_pro)

#extracting bigrams
bi_pro=list(nltk.bigrams(new_words_pro))
bi_con=list(nltk.bigrams(new_words_con))

import pandas as pd
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import sentiwordnet as swn
import matplotlib.pyplot as plt

#finding senders
#extracting senders
data=[]
df = pd.read_csv('H_Clinton-emails.csv', delimiter=',')

#export it as a list of dicts
dicts = df.MetadataFrom

for i in dicts:
        data.append(i)

#REMOVING MEANINGLESS DAYA
data = [datas for datas in data if str(datas) != 'nan']
data = [datas for datas in data if str(datas) != 'H']

# get word frequency for each word
wordfreq = []
for w in data:
    wordfreq.append(data.count(w))

# map frequency to each word
map_freq = zip (data, wordfreq)
map_freq = set(map_freq)
map_freq = list(map_freq)

# sort frequencies according to frequency
sorted_freq = sorted(map_freq, key=lambda x: x[1])

# retrieve last 10 words
freq = sorted_freq[-10:]

#print 10 most frequently used words
print("Most frequently used words are :")
print(freq)

# visulization of emails (top senders)
names = ['McHale, Judith A','PIR','Verma, Richard R','Slaughter, Anne-Marie','Valmoro, Lona J','Jiloty, Lauren C','sbwhoeop','Sullivan, Jacob J','Mills, Cheryl D','Abedin, Huma']
count = ['73','108','115','127','146','302','316','750','1146','1380']

fig = plt.figure()

fig.set_figheight(10)
fig.set_figwidth(10)

plt.bar(names, count, align='center', alpha=0.5)
plt.xticks(names, rotation=90)
plt.ylabel('Number of emails')
plt.xlabel('Top 10 Senders')

plt.show()

#Analyzing words from column A
#extracting data and analyzing from word.txt

# Using regular expressions form nltk
tokenizer = RegexpTokenizer(r'\w+')

a=[]
# Importing file which has all column a data
data1 = open("word.txt")

# Removing Lower case, blank lines and space
data = data1.read().lower().replace("\n", " ")

#Remove Punctuation using tockenizer
data = tokenizer.tokenize(data)


#Removing numerial data( removing unnecessary data )
num_data = []


for i in data:
    if i.isdigit() == False:
        num_data.append(i)

## joining list to perform sentiment analysis
sent=""
sent=' '.join(num_data)


## printing to test word clouds
print("This below text is used for wordcloud")
print(sent)

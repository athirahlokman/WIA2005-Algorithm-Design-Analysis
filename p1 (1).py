from pickle import TRUE
from unittest import result
from numpy import subtract
import plotly.express as px

f = open("Singapore.txt", "r", encoding="utf-8")
wordlist = []
for x in f:
    wordlist += x.split()

# STOPWORD
g = open("stop.txt", "r")
stoplist = []
for x in g:
    stoplist.append(x.strip('\n'))

stopcount = 0
filtered = []
for w in wordlist:
    if w.lower() not in stoplist:
        filtered.append(w)
    else:
        stopcount += 1

print("List\n" + str(wordlist) + "\n")
print("Filtered\n" + str(filtered) + "\n")

wordfreq = []
for w in filtered:
    wordfreq.append(filtered.count(w))
print("Pairs\n" + str(list(zip(filtered, wordfreq))))

# POSITIVE WORD
f = open("positive.txt", "r")
positivelist = []
for x in f:
    positivelist += x.split(",  ")

positivewords = []
for w in filtered:
    if w.upper() in positivelist:
        positivewords.append(w.lower())

posfreq = []
for w in positivewords:
    posfreq.append(positivewords.count(w))
print("\nPositive\n" + str(list(zip(positivewords, posfreq))))
f.close()

#NEGATIVE WORD
k = open("negative.txt", "r", encoding="utf-8")
negativelist = []
for w in k:
    negativelist += w.split(",    ")

negativewords = []
for w in filtered:
    if w.lower() in negativelist:
        negativewords.append(w.lower())

negfreq = []
for w in negativewords:
    negfreq.append(negativewords.count(w))
print("\nNegative\n" + str(list(zip(negativewords, negfreq))))

# NEUTRAL WORDS
k = open("neutral.txt", "r", encoding="utf-8")
neutrallist = []
for w in k:
    neutrallist += w.split(", ")

neutralwords = []
for w in filtered:
    if w.lower() in neutrallist:
        neutralwords.append(w.lower())

neutfreq = []
for w in neutralwords:
    neutfreq.append(neutralwords.count(w))
print("\nNeutral\n" + str(list(zip(neutralwords, neutfreq))))


""" TAK JADIK
#neutrals = []
#neut = positivewords.

negativewords = []
for w in positivewords:
    if w.lower() in negativelist:
        negativewords.append(w.lower())

neut = subtract.array(positivewords, negativewords)
print(neut)

neutralWords = len(positivewords)-len(negativewords)
print("\nNeutral")
print(neutralWords)
"""

#BAR PLOT
#fig = px.bar(x=["positive", "negative", "neutral", "stop"], y=[len(positivewords), len(negativewords), len(neutralwords), stopcount], title="Malaysia wordcount")
#fig.write_html('Malaysia_bar.html', auto_open=True)

#HISTOGRAM
df = neutralwords
fig = px.histogram(df, title="Singapore Neutral Word Histogram")
fig.write_html('Singapore_hist.html', auto_open=TRUE)


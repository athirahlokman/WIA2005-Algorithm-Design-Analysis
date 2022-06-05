f = open("Canada.txt", "r")
wordlist = []
for x in f:
    wordlist += x.split()
 
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
 
f = open("negative.txt", "r")
negativelist = []
for x in f:
    negativelist += x.split(",    ")
 
negativewords = []
for w in filtered:
    if w.lower() in negativelist:
        negativewords.append(w.lower())
 
negfreq = []
for w in negativewords:
    negfreq.append(negativewords.count(w))
print("\nNegative\n" + str(list(zip(negativewords, negfreq))))
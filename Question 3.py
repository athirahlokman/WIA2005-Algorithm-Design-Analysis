# define distance list, sentient list and countries
# 1- Malaysia
# 2- Japan
# 3- Canada
# 4- Singapore
# 5- Qatar

# sentiment score is df['sentiment'] = round((df['pos_count'] - df['neg_count']) / df['total_len'], 2)

import pandas as pd

countrylist = ['MY', 'JP', 'CA', 'SG', 'QA']
listdistance = [1155.1388021283897, 2120.5614364145777, 3133.2066904378166, 36.16260814617173, 35.252065745924874]

# calculate distance score
distanceScore = []
for X in listdistance:
    distScore = (max(listdistance) - X/max(listdistance))
    distanceScore.append(round(distScore, 2))

sentimentScore = [44.2, 13.92, 56.81, 46.98, 68.75]

# scale score of distance and sentient
distanceScoreScaled = []
sentimentScoreScaled = []

for X in distanceScore:
    X_scaled = ((X - min(distanceScore)) / (max(distanceScore) - min(distanceScore))) * 0.25
    distanceScoreScaled.append(round(X_scaled, 4))

for Y in sentimentScore:
    Y_scaled = ((Y - min(sentimentScore)) / (max(sentimentScore) - min(sentimentScore))) * 0.75
    sentimentScoreScaled.append(round(Y_scaled, 4)) 

# calculate probability
prob = []
for i in range(len(distanceScoreScaled)):
    countryProb = (distanceScoreScaled[i]/sum(distanceScoreScaled)) * (sentimentScoreScaled[i]/sum(sentimentScoreScaled))
    prob.append(round(countryProb, 4))

d = {'Country': countrylist, 
    'Distance Score': distanceScoreScaled, 
    'Sentiment Score': sentimentScoreScaled, 
    'Probability': prob}

# perform ranking and summary

df = pd.DataFrame(d)
print(df.sort_values('Probability', ascending=False))

max_index = prob.index(max(prob))

print ("The most probable country is " + countrylist[max_index] + 
" with optimal distance of " + str(round(listdistance[max_index],2)) + 
" km, sentiment score of " + str(sentimentScore[max_index]) + 
" and profit probability of " + str(prob[max_index]))
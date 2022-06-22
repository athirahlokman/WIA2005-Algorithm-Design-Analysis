# sentiment score is df['sentiment'] = round((df['pos_count'] - df['neg_count']) / df['total_len'], 2)

import pandas as pd

#defined list for countries and sentiment score from Q1
countrylist = ['MY', 'JP', 'CA', 'SG', 'QA']
sentimentScore = [44.2, 13.92, 56.81, 46.98, 68.75]

# calculate optimal distance score from Q2
optimalDistanceList = [1155.1388021283897, 2120.5614364145777, 3133.2066904378166, 
                        36.16260814617173, 35.252065745924874]
distanceScore = []
for X in optimalDistanceList:
    distScore = (max(optimalDistanceList) - X) / max(optimalDistanceList)
    distanceScore.append(distScore)


# scale score of distance and sentient between 0 to 1
distanceScoreScaled = []
sentimentScoreScaled = []

for X in distanceScore:
    X_scaled = (X - min(distanceScore)) / (max(distanceScore) - min(distanceScore))
    distanceScoreScaled.append(X_scaled)

for Y in sentimentScore:
    Y_scaled = (Y - min(sentimentScore)) / (max(sentimentScore) - min(sentimentScore))
    sentimentScoreScaled.append(Y_scaled) 

# calculate total score
total_score = []
for i in range(len(distanceScoreScaled)):
    totalScore = distanceScoreScaled[i] * 0.25 + sentimentScoreScaled[i] * 0.75
    total_score.append(round(totalScore,4))

# calculate probability of each score
prob = []
for i in range(len(distanceScoreScaled)):
    countryProb = (total_score[i]/sum(total_score))
    prob.append(round(countryProb, 4))

#define dictionary to store value of each country
d = {'Country': countrylist, 
    'Distance Score': distanceScoreScaled, 
    'Sentiment Score': sentimentScoreScaled, 
    'Total Score': total_score,
    'Probability': prob
    }

# perform ranking 
df = pd.DataFrame(d)
print(df.sort_values('Total Score', ascending=False))

# perform summary
max_index = total_score.index(max(total_score))
print ("The most probable country is " + countrylist[max_index] + 
"\nwith optimal distance of " + str(round(optimalDistanceList[max_index],2)) + 
" km,\nsentiment score of " + str(sentimentScore[max_index]) + 
"\nprofit probability of " + str(prob[max_index]) + 
"\nand total score of " + str(total_score[max_index]))

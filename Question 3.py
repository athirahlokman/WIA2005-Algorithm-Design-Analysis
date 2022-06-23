# sentiment score is df['sentiment'] = round((df['pos_count'] - df['neg_count']) / df['total_len'], 2)

import pandas as pd
import MalaysiaCode;
import JapanCode;
import SingaporeCode;
import QatarCode;
import CanadaCode;
 
#defined list for countries and sentiment score from Q1
countrylist = ['MY', 'JP', 'CA', 'SG', 'QA']
sentimentScores= [MalaysiaCode.sentiment_score, JapanCode.sentiment_score, CanadaCode.sentiment_score, SingaporeCode.sentiment_score, QatarCode.sentiment_score]

# calculate optimal distance score from Q2
optimalDistancesList = [1155.2344770991535, 2326.30263647905, 3136.1746005484483, 
                        36.76437930181419, 35.27253759293162]
distanceScore = []
for X in optimalDistancesList:
    distScore = (max(optimalDistancesList) - X) / max(optimalDistancesList)
    distanceScore.append(distScore)


# scale score of distance and sentient between 0 to 1
def minMaxScaler(inputList, outputList):
    minScore = min(inputList)
    maxScore  = max(inputList)
    for x in inputList:
        scaledScore = (x - minScore) / (maxScore - minScore)
        outputList.append(scaledScore)

sentimentScoreScaled = []
distanceScoreScaled = []
minMaxScaler(sentimentScores, sentimentScoreScaled)
minMaxScaler(distanceScore, distanceScoreScaled)

# calculate total score
total_score = []
for i in range(len(distanceScoreScaled)):
    totalScore = distanceScoreScaled[i] * 0.25 + sentimentScoreScaled[i] * 0.75
    total_score.append(round(totalScore,4))

# calculate probability of each score
prob = []
for i in range(len(total_score)):
    countryProb = (total_score[i]/sum(total_score))
    prob.append(round(countryProb, 4))

#define dictionary to store value of each country
d = {'Country': countrylist,  
    'Sentiment Score': sentimentScoreScaled, 
    'Distance Score': distanceScoreScaled,
    'Total Score': total_score,
    'Probability': prob
    }

# perform ranking 
df = pd.DataFrame(d)
print(df.sort_values('Total Score', ascending=False))

# perform summary
max_index = total_score.index(max(total_score))
print ("The most probable country is " + countrylist[max_index] + 
"\nwith optimal distance of " + str(round(optimalDistancesList[max_index],2)) + 
" km,\nsentiment score of " + str(sentimentScores[max_index]) + 
"\nprofit probability of " + str(prob[max_index]) + 
"\nand total score of " + str(total_score[max_index]))

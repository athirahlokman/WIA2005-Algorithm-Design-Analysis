from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import MalaysiaCode;
import JapanCode;
import SingaporeCode;
import QatarCode;
import CanadaCode;
 
positive_bar = (len(MalaysiaCode.positiveMatch),len(CanadaCode.positiveMatch),len(JapanCode.positiveMatch),len(SingaporeCode.positiveMatch),len(QatarCode.positiveMatch))
negative_bar = (len(MalaysiaCode.negativeMatch),len(CanadaCode.negativeMatch),len(JapanCode.negativeMatch),len(SingaporeCode.negativeMatch),len(QatarCode.negativeMatch))
neutral_bar = (len(MalaysiaCode.neutralMatch),len(CanadaCode.neutralMatch),len(JapanCode.neutralMatch),len(SingaporeCode.neutralMatch),len(QatarCode.neutralMatch))
 
ind = np.arange(5)
 
fig = plt.subplots(figsize=(10,7))
p1 = plt.bar(ind, positive_bar,bottom=negative_bar,width=0.8)
p2 = plt.bar(ind, negative_bar,bottom=neutral_bar,width=0.8)
p3= plt.bar(ind, neutral_bar,width=0.8)
 
plt.ylabel('Frequency')
plt.xlabel('Country')
plt.title('Barplot of Five Countries over Word Count')
plt.xticks(ind,('Malaysia','Canada','Japan','Singapore','Qatar')) #country name
plt.yticks(np.arange(0,400,40))
plt.legend((p1[0],p2[0],p3[0]) , ('Positive','Negative','Neutral'))
 
plt.show()
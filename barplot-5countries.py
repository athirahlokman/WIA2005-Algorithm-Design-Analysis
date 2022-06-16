from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import Omited_Code_Malaysia;
import Omited_Code_Canada;
import Omited_Code_Japan;
import Omited_Code_Singapore;
import Omited_Code_Qatar;

positive_bar = (len(Omited_Code_Malaysia.positiveFound),len(Omited_Code_Canada.positiveFound),len(Omited_Code_Japan.positiveFound),len(Omited_Code_Singapore.positiveFound),len(Omited_Code_Qatar.positiveFound))
negative_bar = (len(Omited_Code_Malaysia.positiveFound),len(Omited_Code_Canada.negativeFound),len(Omited_Code_Japan.negativeFound),len(Omited_Code_Singapore.negativeFound),len(Omited_Code_Qatar.negativeFound))
neutral_bar = (len(Omited_Code_Malaysia.positiveFound),len(Omited_Code_Canada.neutralFound),len(Omited_Code_Japan.neutralFound),len(Omited_Code_Singapore.neutralFound),len(Omited_Code_Qatar.neutralFound))

ind = np.arange(5)

fig = plt.subplots(figsize=(10,7))
p1 = plt.bar(ind, positive_bar,bottom=negative_bar,width=0.8)
p2 = plt.bar(ind, negative_bar,width=0.8)
p3= plt.bar(ind, neutral_bar,bottom=negative_bar,width=0.8)

plt.ylabel('Country')
plt.xlabel('Frequency')
plt.title('Histogram of Five Countries over Word Count')
plt.xticks(ind,('Malaysia','Canada','Japan','Singapore','Qatar')) #country name
plt.yticks(np.arange(0,400,40))
plt.legend((p1[0],p2[0],p3[0]) , ('Positive','Negative','Neutral'))

plt.show()



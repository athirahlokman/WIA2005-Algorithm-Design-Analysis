# WIA2005-Algorithm-Design-Analysis
Group Project codes to compare the economy stability between given countries by comparing positive and negative words in articles using suitable algorithms


#Project Description:
Moonbucks is a coffee chain that has stores located all over the world. The company is constantly looking at running better logistics as well as expansion to open more stores at strategic locations. You and your team have been hired to do analysis and provide insights to the management for making business decisions.  
You have been given a sample dataset that contains the location of Moonbucks stores all over the world. Please use this list to determine the country in Problem 1 and location of store in Problem 2.

Problem 1: 

Moonbucks is always looking at the possibilities of expanding their business by adding the number of stores around the world. To do this, they need to analyse local economic and social situations to ensure maximum profits. 
Select any five (5) countries from the list.

 1. Find five (5) articles from online news websites that have published stories related to each country’s local economy and social situation.
 2. Do an analysis of positive, negative, and neutral words of the article to give insights of the local economic and social situation.
    - Suggestion: Sometimes a webpage must be converted to the text version before it can be done. 
    - You may refer to this website to extract words from a website - https://www.textise.net/. 
    - You may refer to this website on how to count word frequency in a website- https://programminghistorian.org/lessons/counting-frequencies. 
    - You can also filter stop words from the text you found. Stop words are such as conjunctions and prepositions. You may refer to this link:       https://www.ranks.nl/stopwords . 
    - You can find the list of English positive/negative words here - http://positivewordsresearch.com/list-of-positive-words/ ,
    http://positivewordsresearch.com/list-of-negative-words/. 
    - Then, select or design the appropriate string-matching algorithm for the analysis. 

3. Plot line/scatter/histogram graphs related to the word count using Plotly (Word count, stop words)
    - Suggestion: You may refer this link on how to install Plotly and how to use the API keys
    - http://www.instructables.com/id/Plotly-with-Python/ 
    - https://plot.ly/python/getting-started/ 

4. Plot any related graphs to show useful information about the analysis.
5. Give an algorithmic conclusion regarding the sentiment of those articles
Suggestion: If there are more positive words, conclude that the article is giving positive sentiment, if there are more negative words, conclude that the article is giving negative sentiment. You may try to conclude in different perspectives such as whether the list of positive and negative words above is accurate to be used in the context of the article you extracted the text by designing your own algorithm for making conclusions. Based on the conclusion, you may rank which country is worth having branch expansion.



Problem 2: 

Usually, Moonbucks delivers stocks from a warehouse in the region. But recently, the company decided that they want to have a local central distribution center in each country. The stocks will be delivered according to a daily schedule by truck to all the stores in the country. To ensure delivery is optimised, delivery routes will be generated for each of the delivery trucks. 
1. Determine which store to be used for the distribution center in five (5) of the countries used in Problem 1. The store selected must be in the center of at least 5 local stores. 
Suggestion: You can select (randomly) more than six (6) stores in the country and find which store can be used to be the local distribution center.  Select or design an appropriate algorithm for this. You can use Python Geocoding Toolbox, gmplot and Google Distance Matrix API.
2. All deliveries will start from and end at the distribution center. Plot line to show the shortest path for the delivery truck to make an optimal delivery. Keep track of the total distance the truck will be making for the delivery for each of the countries.



Problem 3: 

The expansion of business in a country is not only determined by the local economic and social situation of the country, but the running cost for delivering logistics needs to be considered as well. And usually, a new store location will be determined by how much is spent for delivery. Based on the ranking of countries and total journey made for deliveries of each country, determine the final ranking of countries where new stores can be located.

3. Calculate the probability of a country that has a good local economic and social situation with the lowest optimal delivery. Then, write the summary, ranking from the most recommended countries to the least recommended countries to have an expansion.


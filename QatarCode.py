# String matching algorithm - Trie Algorithm
import plotly.express as px


# TrieNode: to represent a node in the trie
class TrieNode:
    # create instance of nodes in Trie
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_the_end_of_word = False


# Create Trie 
class Trie:
    def __init__(self):  # creating an instance of TrieNode
        self.root = TrieNode("") #create root node with no value

    def add(self, word):
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children: 
                curr_node.children[ch] = TrieNode(ch)  
            curr_node = curr_node.children[ch]
        curr_node.is_the_end_of_word = True  #return true when it reaches the last node in the Trie


    #search matching pattern in Trie
    def search(self, word): 
        if word == "":
            return True #return True if no words checked
        curr_node = self.root 

        for ch in word:
            if ch not in curr_node.children:
                return False  # return false to terminate loop - pattern does not match
            curr_node = curr_node.children[ch]
        return curr_node.is_the_end_of_word  # return true if pattern matched until search is done until last node

# Read text file imported from website

def readArticle(originalText):
    with open('Qatar.txt', 'r', encoding="utf-8") as file:
        for line in file: 
            for word in line.split():
                originalText.append(word)

def readPositive(positive_words):
    with open('positive.txt', 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split(',  '):
                positive_words.append(word)

def readNegative(negative_words):
    with open('negative.txt', 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split(',    '):
                negative_words.append(word)

def readNeutral(neutral_words):
    with open('neutral.txt', 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split(', '):
                neutral_words.append(word)

def readStop(stop_words):
    with open('stop.txt', 'r', encoding="utf-8") as file:
        for line in file:
            for word in line.split('\n'):
                stop_words.append(word)


def refined(lst): 
    formatted = []
    for Line in lst:
        words = Line.split()  
        for i in range(len(words)):
            formatted.append(words[i].replace("\n","")) 
    return formatted

# Driver code
# Call function to read from text file
originalText = []
positive_words = []
negative_words = []
neutral_words = []
stop_words = []

readArticle(originalText)
readPositive(positive_words)
readNegative(negative_words)
readNeutral(neutral_words)
readStop(stop_words)


# To display the article
articleText = refined(originalText) #maybe boleh buang
print("\nList", articleText)

trieStop = Trie()
# Add stop words into the TRIE
for i in range(len(stop_words)):
    trieStop.add(stop_words[i].lower())


stopMatch = []
extractedArticle = [] #articles with no stop words


# Remove stop word
for i in range(len(articleText)):
    if trieStop.search(articleText[i].lower()):
        stopMatch.append(articleText[i])
    else:
        extractedArticle.append(articleText[i])

#call function to create TRIE for each positive, negative and neutral words
triePositive = Trie()
trieNegative = Trie()
trieNeutral = Trie()

# Add positive words into the positive TRIE
for i in range(len(positive_words)):
    triePositive.add(positive_words[i].lower())   #add positive words in lower case

# Add negative words into the negative TRIE
for i in range(len(negative_words)):
    trieNegative.add(negative_words[i].lower())     #add negative words in lower case

# Add neutral words into the neutral TRIE
for i in range(len(neutral_words)):
    trieNeutral.add(neutral_words[i].lower())       #add neutral words in lower case

#array for matching pattern
positiveMatch = []
negativeMatch = []
neutralMatch = []

#search word from extracted article in the TRIE
for i in range(len(extractedArticle)):
    if triePositive.search(extractedArticle[i].lower()):   #search word from extracted article in the positive TRIE
        positiveMatch.append(extractedArticle[i])

    elif trieNegative.search(extractedArticle[i].lower()):  #search word from extracted article in the negative TRIE
        negativeMatch.append(extractedArticle[i])

    elif trieNeutral.search(extractedArticle[i].lower()):   #search word from extracted article in the neutral TRIE
        neutralMatch.append(extractedArticle[i])


print("\nSentence: ", extractedArticle, "\n")
print("Positive: ", positiveMatch, "\n")
print("Negative: ", negativeMatch, "\n")
print("Neutral: ", neutralMatch, "\n")

# Count Word
print("Positive Word: ", len(positiveMatch))
print("Negative Word: ", len(negativeMatch))
print("Neutral Word: ", len(neutralMatch))


a = [len(positiveMatch)]
b = [len(negativeMatch)]
c = [len(neutralMatch)]

number_count = [a,b,c]
type_word = ["Positive", "Negative", "Neutral"]
country_name = ["Qatar"]




from textblob.en.sentiments import NaiveBayesAnalyzer
import scraper
from textblob import TextBlob

#Take topic query
print ("Enter a topic to find polarity on: ")
topic = input()

#Scrape tweets and store in a list
tweetList = scraper.scrapeQuery(topic, 100)

#Adds polarity of 100 tweets on said topic 
totalPolarity = 0;
for text in tweetList:
    totalPolarity += TextBlob(text, analyzer=NaiveBayesAnalyzer()).polarity

#Prints 10 sample negative tweets if the majority of tweets are negative
if (totalPolarity < 0):
    print("Twitter users are displeased with this topic as it has a polarity of %d, here are a few sample negative tweets" % totalPolarity)
    i = 0
    for text in tweetList:
        #A study by JICCE found that Naive Bayes analysis was faster than that of pattern analysis using NLP
        if (TextBlob(text, analyzer=NaiveBayesAnalyzer()).polarity < 0):
            print(text)
            print("\n")
            i += 1
            
        if (i == 10):
            break
        
#Prints 10 sample positive tweets if the majority of tweets are positive
if (totalPolarity > 0):
    print("Twitter users are pleased with this topic as it has a polarity of %d, here are a few sample positive tweets" % totalPolarity)
    i = 0
    for text in tweetList:
        if (TextBlob(text, analyzer=NaiveBayesAnalyzer()).polarity > 0):
            print(text)
            print("\n")
            i += 1
            
        if (i == 10):
            break

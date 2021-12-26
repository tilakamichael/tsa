import scraper
from textblob import TextBlob

print ("Enter a topic to find polarity on: ")
topic = input()

tweetList = scraper.scrapeQuery(topic, 100)

totalPolarity = 0;
for text in tweetList:
    totalPolarity += TextBlob(text).polarity
        
print (totalPolarity)
from tweepy import tweet
import scraper
from textblob import TextBlob

print ("Enter a topic to find polarity on: ")
topic = input()

tweetList = scraper.scrapeQuery(topic, 100)

totalPolarity = 0;
for text in tweetList:
    totalPolarity += TextBlob(text).polarity

if (totalPolarity < 0):
    print("Twitter users are displeased with this topic, here are a few sample negative tweets")
    i = 0
    for text in tweetList:
        if (TextBlob(text).polarity < 0):
            print(text)
            i += 1
            
        if (i == 10):
            break
        
if (totalPolarity > 0):
    print("Twitter users are pleased with this topic, here are a few sample positive tweets")
    i = 0
    for text in tweetList:
        if (TextBlob(text).polarity > 0):
            print(text)
            i += 1
            
        if (i == 10):
            break

print (totalPolarity)
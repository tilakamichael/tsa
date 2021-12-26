from tweepy import tweet
import scraper
from textblob import TextBlob

print ("Enter a topic to find polarity on: ")
topic = input()

tweetList = scraper.scrapeQuery(topic, 100)

totalPolarity = 0;
for text in tweetList:
    totalPolarity += TextBlob(text).polarity

print(totalPolarity)

if (totalPolarity < 0):
    print("Twitter users are displeased with this topic as it has a polarity of %d, here are a few sample negative tweets" % totalPolarity)
    i = 0
    for text in tweetList:
        if (TextBlob(text).polarity < 0):
            print(text)
            print("\n")
            i += 1
            
        if (i == 10):
            break
        
if (totalPolarity > 0):
    print("Twitter users are pleased with this topic as it has a polarity of %d, here are a few sample positive tweets" % totalPolarity)
    i = 0
    for text in tweetList:
        if (TextBlob(text).polarity > 0):
            print(text)
            print("\n")
            i += 1
            
        if (i == 10):
            break

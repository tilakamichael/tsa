import scraper
from textblob import TextBlob

tweetList = scraper.scrapeQuery("Donald Trump", 100)

totalPolarity = 0;
for text in tweetList:
    totalPolarity += TextBlob(text).polarity
        
print (totalPolarity)
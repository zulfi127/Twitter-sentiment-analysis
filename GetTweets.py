import tweepy
import json
import csv
from pprint import pprint

# Step 1 - Authenticate
consumer_key=#######
consumer_secret= ######

access_token=#######
access_token_secret=######

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search(q="@Google", count=100, lang='en')

with open ('get_tweets1b.csv', 'w') as csvfile:
	tweet_writer= csv.writer(csvfile)
	for tweet in public_tweets:
		if (not tweet.retweeted) and ('RT' not in tweet.text):
			parsed_tweet={}
			parsed_tweet['text']= tweet.text
			tweet_writer.writerow([parsed_tweet])

public_tweets2 = api.search(q="@amazon", count=100, lang='en')
with open ('get_tweets2b.csv', 'w') as csvfile:
	tweet_writer= csv.writer(csvfile)
	for tweet in public_tweets2:
		if (not tweet.retweeted) and ('RT' not in tweet.text):
			parsed_tweet={}
			parsed_tweet['text']= tweet.text
			tweet_writer.writerow([parsed_tweet])



public_tweets3 = api.search(q="@apple", count=100, lang='en')
with open ('get_tweets3b.csv', 'w') as csvfile:
	tweet_writer= csv.writer(csvfile)
	for tweet in public_tweets3:
		if (not tweet.retweeted) and ('RT' not in tweet.text):
			parsed_tweet={}
			parsed_tweet['text']= tweet.text
			tweet_writer.writerow([parsed_tweet])	



public_tweets4 = api.search(q="@facebook", count=100, lang='en')
with open ('get_tweets4b.csv', 'w') as csvfile:
	tweet_writer= csv.writer(csvfile)
	for tweet in public_tweets4:
		if (not tweet.retweeted) and ('RT' not in tweet.text):
			parsed_tweet={}
			parsed_tweet['text']= tweet.text
			tweet_writer.writerow([parsed_tweet])


public_tweets5 = api.search(q="@Twitter", count=100, lang='en')
with open ('get_tweets5b.csv', 'w') as csvfile:
	tweet_writer= csv.writer(csvfile)
	for tweet in public_tweets5:
		if (not tweet.retweeted) and ('RT' not in tweet.text):
			parsed_tweet={}
			parsed_tweet['text']= tweet.text
			tweet_writer.writerow([parsed_tweet])



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself




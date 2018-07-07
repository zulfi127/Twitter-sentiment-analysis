import csv
import nltk
import re
from nltk.classify.naivebayes import NaiveBayesClassifier

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist= nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def read_tweets(fname, t_type):
	tweets = []
	with open (fname, 'r') as csvfile:
		data = csv.reader(csvfile)
		for row in data:
			if row[1]== t_type:
				tweets.append([row[0], t_type])
		csvfile.close()
	return tweets

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features ['contains(%s)' % word]= (word in document_words)
	return features


def classify_tweet(tweet):
	return classifier.classify(extract_features(tweet.split()))


pos_tweets = read_tweets('pos_tweets.csv', 'positive')
neg_tweets = read_tweets('neg_tweets.csv', 'negative')


tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	tweets.append((words_filtered, sentiment))


word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)


#print(tweets)
tweet = 'your song is annoying'
print (classifier.classify(extract_features(tweet.split())))

# Evaluate the classifier by test set
test_tweets= read_tweets('tweets_pos_test.csv', 'positive')
test_tweets.extend(read_tweets('tweets_neg_test.csv', 'negative'))
total= accuracy= float(len(test_tweets))



with open ('test_result.csv', 'w') as csvfile:
	data= csv.writer(csvfile)
	for tweet in test_tweets:
		data.writerow((tweet[0], tweet[1], classify_tweet(tweet[0])))

		if classify_tweet(tweet[0])!= tweet[1]:
			accuracy -= 1

print ('Total accuracy: %f%% (%d/200).' % (accuracy / total * 100, accuracy))








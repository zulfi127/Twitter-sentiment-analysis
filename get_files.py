
import csv

def get_files(input_file, pos_output_file, neg_output_file ):
	with open (input_file, 'r') as csvfile:
		with open (pos_output_file, 'w', newline='') as csvfile2:
			with open (neg_output_file, 'w') as csvfile3:
				
				data= csv.reader(csvfile)
				pos_datawriter= csv.writer(csvfile2)
				neg_datawriter= csv.writer(csvfile3)
				for row in data:
					if row[1]=='positive':
						pos_datawriter.writerow(row)
					if row[1]=='negative':
						neg_datawriter.writerow(row)


	return 


get_files('auto_sentiments.csv', 'pos_tweets.csv', 'neg_tweets.csv')

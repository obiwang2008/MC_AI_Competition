# Python program that retrieve the useful info for each article link.
# Hengjia Wang, mastercard, May 29, 2018

import pandas as pd
import csv
from newspaper import Article
import time

df = pd.read_csv("list_google.csv") # read in data
links = df.Links.tolist() # convert to list
n = 1
with open("test.csv",'w') as resultFile:
    for link in links:
        try:
            article = Article(link)
            article.download()
            article.html
            article.parse()
            article.nlp()
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerow([article.title, article.text, article.summary, link, article.authors, article.publish_date, article.keywords])
            print (n)
            n += 1
        except:
            pass
        time.sleep(5) # just to be safe.


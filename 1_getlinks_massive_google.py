# Python program that retrieves the links on the first 100 pages of google news "mastercard" search results.
# Hengjia Wang, mastercard, May 28, 2018

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

search_links = ["https://www.google.com/search?q=mastercard&client=opera&hs=o51&source=lnms&tbm=nws&sa=X&ved=0ahUKEwil3e-6up_bAhVJrlkKHbjNAj4Q_AUICigB&biw=1152&bih=646"] # link for the first page
for i in range(10,1000,10):
    search_links.append("https://www.google.com/search?q=mastercard&client=opera&hs=alM&tbm=nws&ei=v0QHW_ysCNKb5gLFkZK4Dg&start=" + str(i) + "&sa=N&biw=1152&bih=646&dpr=2.5") # links for the 2nd page and beyond.

#print(search_links)


links_data = []
npage = 1
for search_link in search_links:
    print(npage) # helpful
    page = requests.get(search_link)
    soup = BeautifulSoup(page.content, "lxml")
    links = soup.findAll("a")
    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        link = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0]
        links_data.append(link[:link.index("&sa=U")])
    npage += 1
    time.sleep(32) # this is to make sure google does not detect the data scraper. not sure how small this value can be but 32 works.


print (links_data)

links_data = list(set(links_data))
df = pd.DataFrame(links_data, columns=["Links"])
df.to_csv('list_google.csv', index=False) # Save to csv file.


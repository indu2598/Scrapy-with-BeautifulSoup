import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
year = []
rating = []
metascore = []
votes = []
url = 'https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1&ref_=adv_nxt'


page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

listofmoies = soup.find(class_='lister-list')
movies = listofmoies.find_all('div', class_='mode-advanced')
for mov in movies:
    title = mov.find('h3',class_='lister-item-header').find('a')
    yr = mov.find('span', class_='lister-item-year')
    rt = mov.find('div',class_='ratings-imdb-rating').find('strong')
    ms = mov.find('span', class_ = 'metascore favorable')
    vt = mov.find('span',attrs={'name':'nv'})
    if None in (title,yr,rt,ms,vt):
        continue
    titles.append(title.text)
    year.append(yr.text)
    rating.append(rt.text)
    metascore.append(ms.text)
    votes.append(vt.text)
db= pd.DataFrame({'titles':titles,'year':year,'rating':rating,'metascore':metascore,'votes':votes}) 
print(db)
db.to_csv('movie_ratings.csv')

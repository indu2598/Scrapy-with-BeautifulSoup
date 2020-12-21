import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
companys = []
locations = []
url = 'https://www.monster.com/jobs/search/?q=developer&where=Indianapolis__2C-IN&stpage=1&page='
for i in range(1,3):
    page = requests.get(url+str(i))
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')

    serach_result = soup.find(id='ResultsContainer')
    jobs = serach_result.find_all('section', class_='card-content')
    # print(serach_result.prettify())

    # print(jobs[0])
    firstjob = jobs[0]
    for firstjob in jobs:
        title_elem = firstjob.find('h2', class_='title')
        company_elem = firstjob.find('div', class_='company')
        location_elem = firstjob.find('div', class_='location')
        if None in (title_elem,company_elem,location_elem):
            continue
        titles.append(title_elem.text.strip())
        companys.append(company_elem.text.strip())
        locations.append(location_elem.text.strip())
        
#         print(title_elem.text,':-',company_elem.text.strip(),':->',location_elem.text.strip())
#     print("-----------------------------------------------------------------")
db = pd.DataFrame({'titles': titles,'companys':companys,'locations':locations})
print(db.head(5))

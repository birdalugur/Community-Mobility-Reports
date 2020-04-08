
from connect import get_content
from requests import get
import os
from datetime import datetime


current_date = datetime.today().strftime('%Y-%m-%d')



os.mkdir('pdf/'+current_date)


content = get_content('https://www.google.com/covid19/mobility/')


content = content.find('div', class_='glue-expansion-panels')

contents_country = content.find_all('div', class_="country-row")



country_names = [cc.find('h1').text.strip() for cc in contents_country]

pdf_links = [cpdf.find('a', class_="download-link")['href']
             for cpdf in contents_country]



pdf_contents = [get(pc) for pc in pdf_links]



def save(pair):
    name = pair[0]
    pdf = pair[1]
    with open('pdf/'+current_date+'/'+name+'.pdf', 'wb') as f:
        f.write(pdf.content)

for pair in zip(country_names, pdf_contents):
    save(pair)

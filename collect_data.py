

# import csv
import unicodecsv as csv

import urllib2
from bs4 import BeautifulSoup
import chardet

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = 'https://www.ms1timing.com/live_results_v3.php?nocoursse=418&tabformat=RESULT418&where=cla_cat_niv1,105%20km'

page = opener.open(url)
page = page.read()
encoding =  chardet.detect(page)['encoding']

soup = BeautifulSoup(page,from_encoding=encoding)

t = soup.find("table",{"class":"resultats"})

iso_csv = csv.writer(open('data.csv', 'w'))

# get the header rows, write to the CSV
# iso_csv.writerow( t.find("",{'class':'HeaderRow'}).findAll(text=True))


# for row in t.find_all("tr")[0:1]:

#     tds =  row.find_all("td")
#     print [td.findAll(text=True) for td in tds]
#     quit()
# iso_csv.writerow([td.findAll(text=True)[0] for td in t.findAll('td')])





for row in t.find_all("tr")[1:]:
    tds = row.findAll('td')
    raw_cols = [td.findAll(text=True) for td in tds]
    # print raw_cols
    cols = []

    # break     
    # cols.append(raw_cols[0][-1:][0])
    for c in raw_cols:
        if len(c)>0:
            cols.append(str(c[0]))
        else:
            cols.append("")
    # cols.append([str(col) for col in raw_cols])
    # print cols
    iso_csv.writerow(cols)
    # break
quit()


t = soup.find('table', {'class' : 'wikitable sortable'})

# create a new CSV for the output
iso_csv = csv.writer(open('wikipedia-iso-country-codes.csv', 'w'))

# get the header rows, write to the CSV
iso_csv.writerow([th.findAll(text=True)[0] for th in t.findAll('th')])

# Iterate over the table pulling out the country table results. Skip the first 
# row as it contains the already-parsed header information.
data = {}
for row in t.findAll("tr")[1:]:
    tds = row.findAll('td')
    raw_cols = [td.findAll(text=True) for td in tds]
    cols = []
    # country field contains differing numbers of elements, due to the flag -- 
    # only take the name
    cols.append(raw_cols[0][-1:][0])
    # for all other columns, use the first result text
    # print raw_cols[1:3]
    # data[str(raw_cols[2])] = str(raw_cols[1])
    cols.extend([col[0] for col in raw_cols[1:]])
    # print cols
    iso_csv.writerow(cols)

# print data
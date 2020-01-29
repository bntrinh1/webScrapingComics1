#! python3
#downloadXkcd.py - This program is used to download comic strips. Recreational use.

import requests, os, bs4

#starting domain website
url = 'http://xkcd.com'

#stores comic in ./xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.rasie_for_status()

soup = bs4.BeatifulSoup(res.text)

comicElem = soup.select('#comic img')
if comicElem == []:
	print = ('Cant find any comics for you')
else:
	comicUrl = 'http:' + comicElem[0].get('src')
	print('Downloading the comics %s...' % (comicUrl))
	res = requests.get(comicUrl)
	res.raise_for_status()
	imagefile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

prevLink = soup.select('a[rel="prev"]')[0]
url = 'http://xkcd.com' + prevLink.get('href')


print('Done.')
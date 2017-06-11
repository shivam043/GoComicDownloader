import urllib
from bs4 import BeautifulSoup
import os
import sys
import urllib2
def internet_on():
    try:
        urllib2.urlopen('http://www.gocomics.com/comics/popular', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False
if internet_on()==True:
    print("Connection exist...moving forward")
else:   
    print("No connection")
    sys.exit()
dir = os.path.dirname(os.path.abspath(__file__))
gocomicsdir = dir +"/goComics"
if not os.path.exists(gocomicsdir):
    os.makedirs(gocomicsdir)

url=urllib.urlopen("http://www.gocomics.com/comics/popular").read()
soup=BeautifulSoup(url)
tag=soup.find_all('a',{"class":"gc-card-item"},{"href":True})
list_url=[]
list_name=[]
list_urlimg=[]
for l in tag:
   list_url.append(l['href'])
for l in range(len(list_url)):
    url="http://www.gocomics.com"+list_url[l]
    list_name.append(list_url[l][1:])
    url=urllib.urlopen(url).read()
    soup=BeautifulSoup(url)
    tag=soup.find('div',{"data-image":True})
    list_urlimg.append((tag['data-image']))
#downloading begins

for l in range(len(list_name)):
    comicname=list_name[l]
    
    comicdir=dir+"/goComics/"
    filename=comicname
    filepath=os.path.join(comicdir,filename)
    if os.path.isfile(filepath)==True:
        print("Comic already exist "+filename)
        continue
    else:
        print("Downloading "+filename)

    img_data=urllib.urlopen(list_urlimg[l]).read()
    with open (filepath,"wb") as data:
        data.write(img_data)
    
print("Completed downloading  d:")  









#urllib.urlretrieve(tag['data-image'], "00000002.jpg")
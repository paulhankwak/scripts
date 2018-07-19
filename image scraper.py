import requests
import urllib
import time
import os
from bs4 import BeautifulSoup

def getSoup(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    return soup
    
######## start ################
# change to number of pages.
y=0

url = raw_input("Site?: ")
url = str(url)
soup = getSoup(url)

####### Get data needed to find max number of artist post pages 
# html varies from site to site, but as long as button exist for navigating pages this section is still usable
links = soup.find_all('div', attrs={"id", "paginator"})
for link in links[0].find_all('a'):
    splitvar = (link.get('href').split("=",1)[1])
    x = (splitvar.split('&',1)[0])
    x = int(x)
    if (x > y):
        y = x

print "There are "+ str(y) +" Pages."
print "--------------------------------------------------------"

##### Make Directory with artist name

artist_name = url.split("tags=",1)[1]
print artist_name
directory = 'D:\Paul\Downloads\\' + artist_name + '\\'
try: 
    os.makedirs(directory)
except OSError:
    if not os.path.isdir(directory):
        raise

##### Two URL types check for which is used
# urls change too but changable depending.
if (url.find("&") == -1) :
    urlone = url.split("?",1)[0]
    urltwo = url.split("tags",1)[1]
    urlfinal = urlone + "?page={}&tags" + urltwo
else:
    urlone = url.split("=",1)[0]
    urltwo = url.split("&",1)[1]
    urlfinal = urlone + "={}&" + urltwo

##### Iterate through each page
    
for num_url in range(1, y+1):
    url = urlfinal.format(num_url)
    print "------------------- new page ---------"
    print url
    print "--------------------------------------"
    soup = getSoup(url)

    ########## Get Each Posts ##########
    links = soup.find_all('div',attrs={"id" : "posts"})
    posts = links[0].find_all('div')
    for link in posts[0].find_all('a'):
        new_url = ( danboru_main + (link.get('href')))
        
        ##############################
        ########## Individual Posts ##########
        ########## Check for max resolution ##
        ##############################
        
        new_soup = getSoup(new_url)

        resize_link = new_soup.find_all('div', attrs={"id": "image-resize-notice"})
        if (not resize_link):
            resize_link = new_soup.find_all('section', attrs={"id": "image-container"})
            for j in resize_link[0].find_all('img'):
                print(j.get('src'))
                iurl = (j.get('src'))
                imageurl = iurl.split("/__",1)[1]
                print "__"+imageurl

        else:
            for i in resize_link[0].find_all('a'):
                print(i.get('href'))
                iurl = (i.get('href'))
                imageurl = iurl.split("/__",1)[1]
                print "__" + imageurl


print "--------------------------------------------------------"
print "done"
print "--------------------------------------------------------"

                



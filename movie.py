from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
from urllib.request import Request, urlopen

class Movie():

    

    def __init__(self,name,year,file_name,dir,pagename_zipname):
        self.name = name
        self.year = year
        self.file_name = file_name
        self.dir = dir
        self.pagename_zipname = pagename_zipname

    def get_name(self):
        return self.name
    
    def set_pagename_zipname(self,li):
        self.pagename_zipname = li


    def use_selenium(self):
        #usning selenium to get to right page, we need sleep beacuse of the webpage subscene
        # doesn't like if you do things too fast.
        PATH = "C:\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://subscene.com/subtitles/searchbytitle")
        time.sleep(4)
        search = driver.find_element_by_id("query") #locate search bar
        search.send_keys(self.name) #write name
        search.send_keys(Keys.RETURN) #press search

        time.sleep(4)

        title = driver.find_element_by_class_name("title") # pick the first hir
        page = title.find_element_by_css_selector('a').get_attribute('href') #get webpage
        driver.get(page) # go to webpage

        time.sleep(4)
        return driver
        

    def beautiful_soup_scrape(self,driver):
        req = Request(driver.current_url, headers={'User-Agent': 'Mozilla/5.0'})
        sauce = urlopen(req).read()
        soup = bs.BeautifulSoup(sauce,'lxml')

        #we get the table.
        li = []
        x = soup.find_all('tr')
        
        for a in x: 
            #print(a.__dict__)
            print(a.text.encode("utf-8"))
            
            #if a["td class"] == "a40":####här är vi16:40 25/12
            try:
                # get both href and the rest
                li.append([a['href'],str(a.text.encode("utf-8"))])
            except:
                print("UnicodeEncodeError")

        return li


    

#"C:\filmer\Dark.Waters.2019.1080p.WEB-DL.H264.AC3-EVO[TGx]"
#my_movie = Movie(name = "Dark Waters", year = "2019", filename="Dark.Waters.2019.1080p.WEB-DL.H264.AC3-EVO[TGx]",dir =" C:\filmer\Dark.Waters.2019.1080p.WEB-DL.H264.AC3-EVO[TGx]")

#print(my_movie.filename)
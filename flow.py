import time
import zipfile
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string_handling
import zipfile

if __name__ == "__main__":
    # look for thing to happen in folder -> watcher
    data ={}
    while data == {}: # if we get data, we pick it up and end the loop
        # Opening JSON file
        with open('data.json') as json_file:
            data = json.load(json_file)
        time.sleep(1)

    # make the data variables
    name = data["name"]
    year = data["year"]
    file_name = data["file_name"]
    dir = data["dir"]


    #usning selenium to get to right page, we need sleep beacuse of the webpage subscene
    PATH = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://subscene.com/subtitles/searchbytitle")

    time.sleep(4)
    search = driver.find_element_by_id("query")
    search.send_keys(name)
    search.send_keys(Keys.RETURN)

    time.sleep(4)

    title = driver.find_element_by_class_name("title")
    page = title.find_element_by_css_selector('a').get_attribute('href')
    driver.get(page)

    time.sleep(4)

    #beautiful soup to access table info
    ##########################
    import bs4 as bs
    from urllib.request import Request, urlopen
    page = driver.current_url
    req = Request(driver.current_url, headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    #we get the table.
    li = []
    for a in soup.find_all('a', href=True): 
        if a.text: 
            try:
                # get both href and the rest
                li.append([a['href'],str(a.text.encode("utf-8"))])
            except:
                print("UnicodeEncodeError")
            
    #get rid of stuff in the table
    li = string_handling.clean_file(li)
    # split on perferred language. will make it easy to remove the rest. 
    language = "English"
   
    pages = string_handling.pick_language(li,language) 
    #get matches 
    pages = string_handling.get_names_and_matches(pages,file_name)   
    #sort on matches, get most matches first in list
    sorted_pages = string_handling.sort_on_matches(pages)
    #get file name for top picks, decide max amount you want.
    number_of_subs = 4
    page_name,zip_files = string_handling.top_picks_filename(sorted_pages,number_of_subs)


    #visit selected pages and download zip file.
    for page in page_name:
        # '/subtitles/the-peanut-butter-falcon/english/2080151'
        page = "https://subscene.com" + page
        driver.get(page)
        link = driver.find_element_by_link_text("Download English Subtitle")
        link.click()
        time.sleep(1)

    driver.quit()
    

    #extract zipfile to right folder
    for file in zip_files:
        filename = "C:\\Users\\gusta\\Downloads\\" + file
        try: 
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(dir)
        except:
            pass

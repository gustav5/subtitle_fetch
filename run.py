import movie
import time
import json
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

    #with open('data.json', 'w') as outfile:
    #        json.dump({}, outfile)

    cur_movie = movie.Movie(name = data["name"],year = data["year"], file_name = data["file_name"],dir = data["dir"],pagename_zipname = [])

    driver = cur_movie.use_selenium()

    li = cur_movie.beautiful_soup_scrape(driver)

    #get rid of stuff in the table
    li = string_handling.clean_file(li)
    # split on perferred language. will make it easy to remove the rest. 
    language = "English"
    pages = string_handling.pick_language(li,language,cur_movie) 
    #get matches 
    pages = string_handling.get_names_and_matches(cur_movie)   
    #sort on matches, get most matches first in list
    sorted_pages = string_handling.sort_on_matches(pages)
    #get file name for top picks, decide max amount you want.
    number_of_subs = 4
    page_name,zip_files = string_handling.top_picks_filename(sorted_pages,number_of_subs)


    #visit selected pages and download zip file.
    for page in page_name:
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

import movie


def clean_file(li):
    '''remove stuff from each entry
    takes list
    returns clean list
    '''
    for i in range(len(li)):
        li[i][1] = li[i][1].replace("\\n","").replace("\\r","").replace("\\t","").replace("b'","").replace(" '","").replace("English","English,").split(",")

    return li

def pick_language(li,language,cur_movie):
    ''' Selects page name and subtititle filename for given language. 
        put this as a list of dicts in movie object on the form {"page_name": '/subtitles/the-peanut-butter-falcon/english/2488109', "zip_name": 'The.Peanut.Butter.Fa...Rip.Amazon',"n_matches": 0)
        takes list
        
    '''
    li1 = []
    for i in range(len(li)):
        if li[i][1][0] == language:
            li1.append({"page_name": li[i][0], "zip_name": li[i][1][1], "n_matches": 0})

    cur_movie.set_pagename_zipname(li1)
    return li1

def get_names_and_matches(cur_movie):
    #get matches
    pages = []
    file_name_keywords = set(cur_movie.file_name.split("."))
    for i in range(len(cur_movie.pagename_zipname)):
        temp_name = set(cur_movie.pagename_zipname[i]["zip_name"].split("."))

        number_of_matches = len(temp_name.intersection(file_name_keywords))
        cur_movie.pagename_zipname[i]["n_matches"] = number_of_matches
    return pages


def sort_on_matches(pages):
    #sort on matches, get most matches first in list
    sorted_pages = sorted(pages, key=lambda x: x[2])
    sorted_pages.reverse()
    return sorted_pages

def top_picks_filename(sorted_pages,number_of_subs):
    #get file name for top picks
    top_picks_filename = []
    page_name = []
    for i in range(number_of_subs):
        name =sorted_pages[i][0].split("/")
        top_picks_filename.append(name[2] + "_" + name[3] +"-" +name[4] + ".zip")
        page_name.append(sorted_pages[i][0])
    return page_name,top_picks_filename


            

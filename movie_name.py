
def get_movie_title_and_year(name):
    '''Takes a folder name, and returns name of movie and year it was made, in a string'''
    #naming can be done differently, but the first thing in the folder name is the moive name i think.
    name = name.split("\\")[-1]
    #either the name and year is separated by "." or " ".
    movie_name = ""
    if " " in name:
        name= name.split(" ")
        for i in range(len(name)):
            if "(" in name[i]:
                movie_name = " ".join(name[:i+1]).replace("(","").replace(")","")
    else:
        name= name.split(".")
        for i in range(1,len(name)):
            try: 
                year = int(name[i]) #possible year
                if year in range(1900,2022): #resonable years 
                    if not name[i+1].isdigit(): #check so that the title of the movie it self isn't a year.
                        movie_name = " ".join(name[:i+1]) 
            except:
                pass
    
    return movie_name


def get_file_name(name):
    """name of files can be dot separated or space separated
    We get a folder dir as input, where the last part is the name

        Returns a two-coloring of the graph.
    Raises an exception if the graph is not bipartite.
    Parameters
    ----------
    A directory name: String.
    example: "C:\filmer\Dark.Waters.2019"

    Returns
    -------
    name of the movie: String
    Movie.Name.2019
    """

    name = name.split("\\")[-1]
    #if ". separated we already have a filename"
    if "." in name:
        return name

    

if __name__ == "__main__":
    get_movie_title_and_year()

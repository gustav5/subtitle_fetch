import watchdog.events
import watchdog.observers
import movie_name
import json

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=["*"], ignore_patterns = None, ignore_directories = False, case_sensitive = True)
        
    def on_created(self, event):
        print(f"File created at : {event.src_path}")
        dir = str(event.src_path) #name of dir
        file_name = movie_name.get_file_name(dir.split("\\")[-1]) 
        #to get name, split path on "\"" and pick last one. 
        name_year = movie_name.get_movie_title_and_year(dir)
        year = name_year
        name = " ".join(name_year.split(" ")[:-1])
        year = name_year.split(" ")[-1]

        #write this to a json file
        dict1 = { "name": name, "year":year, "dir":dir, "file_name": file_name}
        with open('data.json', 'w') as outfile:
            json.dump(dict1, outfile)

    def on_deleted(self, event):
        print(f"File deleted : {event.src_path}")

event_handler = Handler()
observer = watchdog.observers.Observer()
observer.schedule(event_handler, r"C:\filmer", recursive = False) #val av mapp

observer.start()
observer.join()

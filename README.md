# subtitle_fetch
Downloads subtitles from subscene for your legally downloaded movies. Just a project I done on my own. Wanted to automate somthing and this is what i came up with. The program will perform the following:
- Detect that a new directory has appered in a chosen movies directory with watchdog.
- Pick the information from the directory/file name and get a movie name and a file name.
- Go to the webpage subscene with Selenium and search for the movie and click on the first pick.
- Scrape the table with info about subtitles with requests.
- Pick the chosen language.
- Pick the top 4 subtile files that has most matches on the directory name.
- Download these with selenium
- Unzip from downloads directory to the right movie directory.

I got it working, but I'm trying to make the code better. This was harder than i thought. Some things I am working on:
- I did a lot of lists, changing these to dictionarys instead. 
- Making the movie an object with attributes and some methods.
- Changing from beautiful soup to requests to scrape subscene.


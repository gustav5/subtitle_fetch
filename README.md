# subtitle_fetch
Downloads subtitles from subscene for your legally downloaded movies. Just a project I done on my own. Wanted to automate somthing and this is what i came up with. 
- Detecet that a new directory has apperd in a chosen movies directory
- It will pick the information from the directory/file name and get a movie name
- Go to the webpage subscene with Selenium and search for the movie and click on the first pick 
- Scrape the table with info about subtitles
- Pick the chosen language
- Pick the top 4 subtile files that has most matches on the directory name.
- Download these with selenium
- Unzip from downloads directory to the right movie directory.

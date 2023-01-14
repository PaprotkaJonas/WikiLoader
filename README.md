# WikiLoader
WikiLoader is a Python script that makes it easy to scrape Wikipedia data.
----------------------------------------------------------------------------

WikiLoader is a Python script that allows you to easily scrape Wikipedia data for multiple keywords and save it as a JSON file. The script uses the wikipedia and wikipediaapi libraries to search and extract data. You can easily configure the script by editing the settings in the main.py file, including the keywords to search for, the number of results per keyword, the language of the Wikipedia page, and the location to save the JSON files. The script also keeps track of the time it takes to scrape each keyword and the total time it takes to scrape all keywords. The script also skips keywords that have already been scraped and saved in the specified location.

----------------------------------------------------------------------------

# Config

in the 'main.py':

------------------------------

search = ["Python", "Github"]

results_per_tag = 100

summary = True

my_language = "en"

location = "data"

------------------------------

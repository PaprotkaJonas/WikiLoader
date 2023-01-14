import json
import os
import os.path
import time

import wikipedia
import wikipediaapi

########### Settings ###########
search = ["Python", "Github", "Wikipedia"]
results_per_tag = 100
summary = True
my_language = "en"
location = "data"
########### Settings ###########

track_start_time = time.time()

my_wiki = wikipediaapi.Wikipedia(
    language=my_language,
    extract_format=wikipediaapi.ExtractFormat.WIKI)

search_sum = len(search)
alrd = 1
skipped_elements = 0

for i in search:
    start_time = time.time()
    if os.path.isfile(f'{location}/{i}.json'):
        alrd +=1
        skipped_elements += 1
        continue
    else:
        the_data={}
        if summary == True:
            for items in wikipedia.search(i, results=results_per_tag):
                the_data[items] = my_wiki.page(items).summary
        else:
            for items in wikipedia.search(i, results=results_per_tag):
                the_data[items] = my_wiki.page(items).text
        with open(f"data/{i}.json", "w") as f:
            json.dump(the_data, f, indent=4)
        f.close()
        os.system('cls')
        print(f"[{results_per_tag}={i}], [lang={my_language}], [location='{location}']\n[{alrd}|{search_sum}], [{round(time.time() - start_time, 2)} Seconds]")
        alrd += 1
os.system('cls')
print(f"[loaded={search}]\n[{alrd-1}|{search_sum}], [skipped={skipped_elements}], [{round(time.time() - track_start_time, 2)} Seconds]\n\n[location='{location}']\n\n")
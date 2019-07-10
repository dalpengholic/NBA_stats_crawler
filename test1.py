from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import string
import io
import sys
import os
import json
from datetime import datetime
from multiprocessing import Pool

''' This module is desinged to collect the number of nba players and each of 
player's URL from https://www.basketball-reference.com.

First, collect the number of players starting with first letter of 
their last name. For example, the player 'Kareem Abdul-Jabbar' is in 
the list of A letter list.



'''
startTime = datetime.now()
opener = req.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0")]
req.install_opener(opener)

# Get a list of the url addresses from a to z
url_base = "https://www.basketball-reference.com/players/"
alphabet = list(string.ascii_lowercase)
del alphabet[-3]

# Make a beautifulsoup object
number_of_players_list = []
for i in alphabet:
    res = req.urlopen(url_base+i+"/") # the URL starting with 'i' letter of last name.
    soup = BeautifulSoup(res,"html.parser")
    parsed_number_string = soup.select("#all_players > div.section_heading > h2")

    for j in parsed_number_string:
        number_of_players_list.append(j.string[:-8])
        print(number_of_players_list)

# Make dictionary initials with corresponding numbers
initial_number_dic = dict(zip(alphabet, number_of_players_list))
print(initial_number_dic)

# Save to a json file.
with open('number_of_NBA_players.json', 'w') as f:
    f.write(json.dumps(initial_number_dic,indent=4))
print(datetime.now() - startTime)


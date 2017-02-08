import pandas as pd
print("pandas version: %s" % pd.__version__)

import matplotlib
print("matplotlib version: %s" % matplotlib.__version__)

import numpy as np
print("numpy version: %s" % np.__version__)

import IPython
print("IPython version: %s" % IPython.__version__)

import sklearn
print("scikit-learn version: %s" % sklearn.__version__)

import pygame
print("pygame version: %s" % pygame.__version__)

############################################################################################
#import  requests_cache
import requests

import dataset
db = dataset.connect('sqlite:///data_wrangling.db')
my_data_source = {
    'url':
    'http://www.tsmplug.com/football/premier-league-player-salaries-club-by-club/',
    'description': 'Premier League Club Salaries',
    'topic': 'football',
    'verified': False,
}
table = db['data_sources']
table.insert(my_data_source)
another_data_source = {
    'url':
    'http://www.premierleague.com/content/premierleague/en-gb/players/index.html',
    'description': 'Premier League Stats',
    'topic': 'football',
    'verified': True,
}
table.insert(another_data_source)
sources = db['data_sources'].all()
print (sources)
print (sources.row_type)

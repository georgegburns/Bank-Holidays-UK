import os

import pandas as pd
import requests

URL = 'https://www.gov.uk/bank-holidays.json'
DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 

res = requests.get(URL)
data = res.json()

ENGLAND = pd.DataFrame(data['england-and-wales']['events'])
SCOTLAND = pd.DataFrame(data['scotland']['events'])
NI = pd.DataFrame(data['northern-ireland']['events'])

ENGLAND['Country'] = 'England & Wales'
SCOTLAND['Country'] = 'Scotland'
NI['Country'] = 'Northern Ireland'

COUNTRIES = [ENGLAND, SCOTLAND, NI]
HOLIDAYS = pd.concat(COUNTRIES)
HOLIDAYS.drop(['notes', 'bunting'], axis=1, inplace=True)
COLUMNS = {'title': 'Holiday', 'date':'Date', 'Country': 'Country'}
HOLIDAYS.rename(columns=COLUMNS, inplace=True)
HOLIDAYS['Date'] = pd.to_datetime(HOLIDAYS['Date'], yearfirst=True)

HOLIDAYS.to_excel(DESKTOP + '/Bank Holidays.xlsx', index=False)
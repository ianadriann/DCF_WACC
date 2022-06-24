from numpy import dtype
from pyrsistent import b
import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data
import datetime
#from datetime import datetime, timedelta
import numpy_financial as npf
import Income_statement


#URL
url_financials_is = 'https://finance.yahoo.com/quote/{}/financials?p={}'

#Variable
ticker_code = 'AAPL'

#headers
headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36' }
response = requests.get(url_financials_is.format(ticker_code, ticker_code),headers={'user-agent':'my-app'})

#scriping
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])

#location variable of yahoo
I_S = json_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']
I_S_totalOtherIncomeExpensesNet = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']

input1 = 'lastyear'
Income_statement1 = Income_statement.date_is_annual(input1, I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)

iis = pd.DataFrame.from_dict(Income_statement1,orient='index')
print(iis[0]['grossProfit'])
'''
yearago = 0
yearago_2 = -1
Income_statement_coba = Income_statement

iis_coba = pd.DataFrame.from_dict(Income_statement_coba, orient='index')
print(iis_coba[0]['grossProfit'])
'''
input2 = 'twoyearago'
Income_statement2 = Income_statement.date_is_annual(input2, I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)

iis2 = pd.DataFrame.from_dict(Income_statement2,orient='index')
print(iis2[0]['grossProfit'])




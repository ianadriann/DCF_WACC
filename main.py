from distutils.log import error
import traceback
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

#lastyear, yearago, years2ago, years3ago
is_1 = Income_statement.date_is_annual('lastyear', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
is_2 = Income_statement.date_is_annual('yearago', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
is_3 = Income_statement.date_is_annual('years2ago', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
is_4 = Income_statement.date_is_annual('years3ago', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
IS = [is_1, is_2, is_3, is_4]


revenue_g = (IS[0]['revenue'] - IS[1]['revenue']) / IS[1]['revenue']
revenue_g1 = ((IS[0]['revenue'] / IS[3]['revenue'])**(1/3))-1
revenue_g2 = ((IS[0]['revenue'] / IS[3]['revenue'])-1)/3
income_statement = pd.DataFrame.from_dict(IS[0],orient='index')
income_statement = income_statement[8:36]
income_statement.columns = ['current_year']
income_statement['as_%_of_revenue'] = income_statement / income_statement.iloc[0]


#model prediksi tahun berikutnya
income_statement['next_year'] = (income_statement['current_year']['revenue'] * (1 + revenue_g)) * income_statement['as_%_of_revenue']

#print(income_statement)
'''
nilai akhir = 19000
nilai awal = 10000
tahun = 3
a = (((19000/10000)**(1/3))-1)*100
'''
print(revenue_g*100)
print(revenue_g1*100)
print(revenue_g2*100)

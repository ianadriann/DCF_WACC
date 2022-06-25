from numpy import dtype
from pyrsistent import b
import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data
#import datetime
from datetime import timedelta, date
import numpy_financial as npf
import Income_statement
import balancesheet
import freecashflow
import RFandICA


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
I_S_start = json_data['context']['dispatcher']['stores']
I_S = I_S_start['QuoteTimeSeriesStore']['timeSeries']
#I_S_totalOtherIncomeExpensesNet = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
I_S_totalOtherIncomeExpensesNet = I_S_start['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']

#lastyear, yearago, years2ago, years3ago
is_1 = Income_statement.date_is_annual('lastyear', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
is_2 = Income_statement.date_is_annual('yearago', I_S_totalOtherIncomeExpensesNet, I_S, ticker_code)
IS = [is_1, is_2]


revenue_g = (IS[0]['revenue'] - IS[1]['revenue']) / IS[1]['revenue']
income_statement = pd.DataFrame.from_dict(IS[0],orient='index')
income_statement = income_statement[8:36]
income_statement.columns = ['current_year']
income_statement['as_%_of_revenue'] = income_statement / income_statement.iloc[0]

#model prediksi tahun berikutnya
income_statement['next_year'] = (income_statement['current_year']['revenue'] * (1 + revenue_g)) * income_statement['as_%_of_revenue']
income_statement['next_2_year'] =  (income_statement['next_year']['revenue'] * (1+revenue_g)) * income_statement['as_%_of_revenue'] 
income_statement['next_3_year'] =  (income_statement['next_2_year']['revenue'] * (1+revenue_g)) * income_statement['as_%_of_revenue'] 
income_statement['next_4_year'] =  (income_statement['next_3_year']['revenue'] * (1+revenue_g)) * income_statement['as_%_of_revenue'] 
income_statement['next_5_year'] =  (income_statement['next_4_year']['revenue'] * (1+revenue_g)) * income_statement['as_%_of_revenue']


#screaping balanceSheet YF
url_balanceSheet = 'https://finance.yahoo.com/quote/{}/balance-sheet?p={}'
response_balanceSheet = requests.get(url_balanceSheet.format(ticker_code, ticker_code),headers={'user-agent':'my-app'})

soup_balanceSheet= BeautifulSoup(response_balanceSheet.text, 'html.parser')
pattern_balanceSheet= re.compile(r'\s--\sData\s--\s')
script_data_balanceSheet= soup_balanceSheet.find('script', text=pattern_balanceSheet).contents[0]
start_balanceSheet = script_data_balanceSheet.find("context")-2
json_data_balanceSheet = json.loads(script_data_balanceSheet[start_balanceSheet:-12])

B_S_start = json_data_balanceSheet['context']['dispatcher']['stores']
B_S = B_S_start['QuoteTimeSeriesStore']['timeSeries']
balanceSheetHistoryQuarterly = B_S_start['QuoteSummaryStore']['balanceSheetHistoryQuarterly']

bs_1 = balancesheet.date_bs_annual('lastyear', I_S_totalOtherIncomeExpensesNet, B_S, I_S, ticker_code)
bs_2 = balancesheet.date_bs_annual('yearago', I_S_totalOtherIncomeExpensesNet, B_S, I_S, ticker_code)


BS = [bs_1,bs_2]
balance_sheet = pd.DataFrame.from_dict(BS[0],orient='index')
balance_sheet = balance_sheet[8:-2]
balance_sheet.columns = ['current_year']
balance_sheet['as_%_of_revenue'] = balance_sheet / income_statement['current_year'].iloc[0]

#model prediksi tahun berikutnya
balance_sheet['next_year'] = income_statement['next_year']['revenue'] * balance_sheet['as_%_of_revenue']
balance_sheet['next_2_year'] = income_statement['next_2_year']['revenue'] * balance_sheet['as_%_of_revenue'] 
balance_sheet['next_3_year'] = income_statement['next_3_year']['revenue'] * balance_sheet['as_%_of_revenue'] 
balance_sheet['next_4_year'] = income_statement['next_4_year']['revenue'] * balance_sheet['as_%_of_revenue'] 
balance_sheet['next_5_year'] = income_statement['next_5_year']['revenue'] * balance_sheet['as_%_of_revenue']

#model free cash flow
CF_forecast = freecashflow.freecashflow(income_statement, balance_sheet)
CF_forec = pd.DataFrame.from_dict(CF_forecast, orient='columns')

#add below option to format the dataframe with thousand separators
pd.options.display.float_format = '{:,.0f}'.format

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
startdate = date(2020, 12, 31)
#end= date.today().strftime('%Y-%m-%d')
enddate = date(2021, 12, 31)
'''
#end = today, start = year of today
enddate = date.today()
enddate = enddate.strftime('%Y-%m-%d')
startdate = date.today() - timedelta(days=365)
startdate = startdate.strftime('%Y-%m-%d')
'''

RF_ICA = RFandICA.interest_coveraga_and_RF(IS, startdate, enddate)

RF = RF_ICA[0]
interest_coverage_ratio = RF_ICA[1]
cost_of_debt = RFandICA.cost_of_debt(RF, interest_coverage_ratio)

#beta
beta = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['summaryDetail']['beta']['raw']

#index
index_SP500 = data.DataReader("^GSPC", start=startdate + timedelta(days=1), end=enddate, data_source='yahoo')['Adj Close']
#index_IHSG = data.DataReader("^JKSE", start=start, end=end, data_source='yahoo')['Adj Close']
cost_of_equity = RFandICA.costofequity(RF, beta, index_SP500)

WACC = RFandICA.waccDate(IS, ticker_code, balanceSheetHistoryQuarterly, cost_of_equity, cost_of_debt)

print('revenue_g = ', revenue_g)
print('RF = ', RF)
print('cost_of_debt = ', cost_of_debt)
print('cost_of_equity = ', cost_of_equity)
print('WACC =', WACC)



print('='*20)




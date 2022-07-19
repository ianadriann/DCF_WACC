import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from pandas_datareader import data
from datetime import timedelta, date
import numpy_financial as npf
import Income_statement
import balancesheet
import freecashflow
import RFandICA


#URL
url_financials_is = 'https://finance.yahoo.com/quote/{}/financials?p={}'

#Variable
ticker_code = 'AAPL' #aapl= 229.69779556090393

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

#lastyear, yearago, years2ago, years3ago
is_1 = Income_statement.date_is_annual('lastyear', I_S_start, ticker_code)
is_2 = Income_statement.date_is_annual('yearago', I_S_start, ticker_code)
IS = [is_1, is_2]


revenue_g = (IS[0]['revenue'] - IS[1]['revenue']) / IS[1]['revenue']
income_statement = pd.DataFrame.from_dict(IS[0],orient='index')
income_statement = income_statement #[8:36] #if u allow all variable in income_statement.py
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


bs_1 = balancesheet.date_bs_annual('lastyear', B_S_start, I_S_start, ticker_code)
bs_2 = balancesheet.date_bs_annual('yearago', B_S_start, I_S_start, ticker_code)


BS = [bs_1,bs_2]
balance_sheet = pd.DataFrame.from_dict(BS[0],orient='index')
balance_sheet = balance_sheet#[8:-2] #if u allow all variable in income_statement.py
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
beta = I_S_start['QuoteSummaryStore']['summaryDetail']['beta']['raw']

#index
index_SP500 = data.DataReader("^GSPC", start=startdate + timedelta(days=1), end=enddate, data_source='yahoo')['Adj Close']
#index_IHSG = data.DataReader("^JKSE", start=start, end=end, data_source='yahoo')['Adj Close']
cost_of_equity = RFandICA.costofequity(RF, beta, index_SP500)

WACC1 = RFandICA.waccDate(IS, ticker_code, B_S_start, cost_of_equity, cost_of_debt)
WACC = WACC1[0]

#Net Present Value of the Forecasted Free Cash Flows
FCF_List = CF_forec.iloc[-1].values.tolist()
npv = npf.npv(WACC, FCF_List)

#Terminal value
LTGrowth = 0.02
Terminal_value = (CF_forecast['next_5_year']['FCF'] * (1+ LTGrowth)) /(WACC  - LTGrowth)
Terminal_value_Discounted = Terminal_value/(1+WACC)**4

#Calculating ticker_code Target Price
target_equity_value = Terminal_value_Discounted + npv
debt = balance_sheet['current_year']['totalDebt']
target_value = target_equity_value - debt
numbre_of_shares = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualBasicAverageShares'][-1]['reportedValue']['raw']
target_price_per_share = target_value/numbre_of_shares

print('revenue_g = ', revenue_g)
print('RF = ', RF)
print('cost_of_debt = ', cost_of_debt)
print('cost_of_equity = ', cost_of_equity)
print('WACC =', WACC)
print('npv = ', npv)
print('Terminal_value_Discounted =', Terminal_value_Discounted)

print('='*20)
print('the forecast is based on the following assumptions: '+ 'revenue growth: ' + str(revenue_g) + ' Cost of Capital: ' + str(WACC) )
print('perpetuity growth: ' + str(LTGrowth)  )
print((f'{ticker_code}') + ' forecasted price per stock is ' + str(target_price_per_share) )

EBIT= IS[0]['ebitda'] - IS[0]['depreciationAndAmortization']
interest_expense = IS[0]['interestExpense']
interest_coverage_ratio = EBIT / interest_expense
print(EBIT, interest_expense, interest_coverage_ratio)




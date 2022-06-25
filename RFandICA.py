import pandas_datareader.data as web
import yfinance as yf


def interest_coveraga_and_RF(IS, start, end):
    EBIT= IS[0]['ebitda'] - IS[0]['depreciationAndAmortization']
    interest_expense = IS[0]['interestExpense']
    interest_coverage_ratio = EBIT / interest_expense

    #RF
    Treasury = web.DataReader(['TB1YR'], 'fred', start, end)
    RF = float(Treasury.iloc[-1])
    RF = RF/100
    return [RF, interest_coverage_ratio]
    
def cost_of_debt(RF, interest_coverage_ratio):
    #Cost of debt
    if interest_coverage_ratio > 12.5:
        #Rating is AAA
        credit_spread = 0.0067
        
    if (interest_coverage_ratio > 6.5) & (interest_coverage_ratio <= 12.5):
        #Rating is AA
        credit_spread = 0.0082
        
    if (interest_coverage_ratio > 7.5) & (interest_coverage_ratio <=  6.5):
        #Rating is A+
        credit_spread = 0.0103
        
    if (interest_coverage_ratio > 6) & (interest_coverage_ratio <=  7.5):
        #Rating is A
        credit_spread = 0.0114
        
    if (interest_coverage_ratio > 4.5) & (interest_coverage_ratio <=  6):
        #Rating is A-
        credit_spread = 0.0129
        
    if (interest_coverage_ratio > 4) & (interest_coverage_ratio <=  4.5):
        #Rating is BBB
        credit_spread = 0.0159
        
    if (interest_coverage_ratio > 3.5) & (interest_coverage_ratio <=  4):
        #Rating is BB+
        credit_spread = 0.0193
        
    if (interest_coverage_ratio > 3) & (interest_coverage_ratio <=  3.5):
        #Rating is BB
        credit_spread = 0.0215
        
    if (interest_coverage_ratio > 2.5) & (interest_coverage_ratio <= 3):
        #Rating is B+
        credit_spread = 0.0315
        
    if (interest_coverage_ratio > 2) & (interest_coverage_ratio <=  2.5):
        #Rating is B
        credit_spread = 0.0378
        
    if (interest_coverage_ratio > 1.5) & (interest_coverage_ratio <=  2):
        #Rating is B-
        credit_spread = 0.0462
        
    if (interest_coverage_ratio > 1.25) & (interest_coverage_ratio <=  1.5):
        #Rating is CCC
        credit_spread = 0.0778
        
    if (interest_coverage_ratio > 0.8) & (interest_coverage_ratio <=  1.25):
        #Rating is CC
        credit_spread = 0.0880
        
    if (interest_coverage_ratio > 0.5) & (interest_coverage_ratio <=  0.8):
        #Rating is C
        credit_spread = 0.1076
    if interest_coverage_ratio <=  0.5:
        #Rating is D
        credit_spread = 0.1434

    cost_of_debt = RF + credit_spread
    return cost_of_debt

def costofequity(RF, beta, SP500):
    #SP500 = data.DataReader("^GSPC", start=startdate + timedelta(days=1), end=enddate, data_source='yahoo')['Adj Close']
    SP500.dropna(inplace = True)
    SP500yearlyreturn = (SP500.iloc[-1]/ SP500.iloc[-252])-1
    cost_of_equity = RF+(beta*(SP500yearlyreturn - RF))
    return cost_of_equity

def waccDate(IS, ticker_code, balanceSheetHistoryQuarterly, cost_of_equity, cost_of_debt):
    netIncome = IS[0]['netIncome']
    incomeBeforeTax = IS[0]['incomeBeforeTax']
    totaltax = incomeBeforeTax - netIncome
    ETR = totaltax/incomeBeforeTax
    ticker= yf.Ticker(ticker_code)
    info_comp = ticker.info
    totalDebt = info_comp['totalDebt']
    totalStockholdersEquity = balanceSheetHistoryQuarterly['balanceSheetStatements'][0]['totalStockholderEquity']['raw']
    Debt_to = totalDebt / (totalDebt + totalStockholdersEquity)
    equity_to = totalStockholdersEquity / (totalDebt + totalStockholdersEquity)

    WACC = (cost_of_debt*(1-ETR)*Debt_to) + (cost_of_equity*equity_to)
    return WACC




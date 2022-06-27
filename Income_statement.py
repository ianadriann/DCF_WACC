## for US
### for Indonesia >erase> annualInterestExpenseNonOperating


def date_is_annual(input1, I_S_start, ticker_code):
    if input1 == 'lastyear':
        year = 0
        input2 = -1
    elif input1 == 'yearago':
        year = 1
        input2 = -2
    elif input1 ==  'years2ago':
        year = 2
        input2 = -3
    elif input1 ==  'years3ago':
        year = 3
        input2 = -4
    elif input1 ==  'years4ago':
        year = 4
        input2 = -5
    else:
        print('out of index')
    #old
    date = I_S_start['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory'][year]['endDate']['fmt']
    ###reportedCurrency = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOperatingExpense'][input2]['currencyCode']
    revenue = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalRevenue'][input2]['reportedValue']['raw']
    ###costOfRevenue = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualReconciledCostOfRevenue'][input2]['reportedValue']['raw']
    ###grossProfit = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGrossProfit'][input2]['reportedValue']['raw']
    ##researchAndDevelopmentExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualResearchAndDevelopment'][input2]['reportedValue']['raw'] #hapus
    #generalAndAdministrativeExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGeneralAndAdministrativeExpense'][input2]['reportedValue']['raw']
    #SellingAndMarketingExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualSellingAndMarketingExpense'][input2]['reportedValue']['raw']
    sellingGeneralAndAdministrativeExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualSellingGeneralAndAdministration'][input2]['reportedValue']['raw']
    ###operatingExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOperatingExpense'][input2]['reportedValue']['raw']
    ###costAndExpenses = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalExpenses'][input2]['reportedValue']['raw']
    ##interestIncome = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInterestIncomeNonOperating'][input2]['reportedValue']['raw']
    interestExpense = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInterestExpenseNonOperating'][input2]['reportedValue']['raw']
    depreciationAndAmortization = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualReconciledDepreciation'][input2]['reportedValue']['raw']
    ebitda = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNormalizedEBITDA'][input2]['reportedValue']['raw']
    ##operatingIncome = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalOperatingIncomeAsReported'][input2]['reportedValue']['raw']
    totalOtherIncomeExpensesNet = I_S_start['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory'][year]['totalOtherIncomeExpenseNet']['raw']
    incomeBeforeTax = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualPretaxIncome'][input2]['reportedValue']['raw']
    ##incomeTaxExpense = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTaxProvision'][input2]['reportedValue']['raw']
    netIncome = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetIncome'][input2]['reportedValue']['raw']
    eps = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualBasicEPS'][input2]['reportedValue']['raw']
    epsdiluted = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualDilutedEPS'][input2]['reportedValue']['raw']
    weightedAverageShsOut = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualBasicAverageShares'][input2]['reportedValue']['raw']
    weightedAverageShsOutDil = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualDilutedAverageShares'][input2]['reportedValue']['raw']
    
    #variable
    income_statement = {}
    '''
    income_statement['date'] = date 
    income_statement['symbol'] = ticker_code
    income_statement['reportedCurrency'] = reportedCurrency
    income_statement['cik'] = 'cik'
    income_statement['fillingDate'] = 'fillingDate'
    income_statement['acceptedDate'] = 'xxxxxx'
    income_statement['calendarYear'] = date
    income_statement['period'] = 'FY'
    '''
    income_statement['revenue'] = revenue
    ###income_statement['costOfRevenue'] = costOfRevenue
    ###income_statement['grossProfit'] = grossProfit
    ###income_statement['grossProfitRatio'] = (revenue-costOfRevenue)/revenue
    ##income_statement['researchAndDevelopmentExpenses'] = researchAndDevelopmentExpenses #hapus
    #income_statement['generalAndAdministrativeExpenses'] = generalAndAdministrativeExpenses
    income_statement['generalAndAdministrativeExpenses'] = 0.0
    #income_statement['annualSellingAndMarketingExpenses'] = annualSellingAndMarketingExpenses
    income_statement['sellingAndMarketingExpenses'] = 0.0
    income_statement['sellingGeneralAndAdministrativeExpenses'] = sellingGeneralAndAdministrativeExpenses
    income_statement['otherExpenses']=0.0
    ###income_statement['operatingExpenses'] = operatingExpenses
    ###income_statement['costAndExpenses'] =  costAndExpenses
    ##income_statement['interestIncome'] = interestIncome
    income_statement['interestExpense'] = interestExpense
    income_statement['depreciationAndAmortization'] = depreciationAndAmortization
    income_statement['ebitda'] = ebitda
    income_statement['ebitdaratio'] = ebitda / revenue
    ##income_statement['operatingIncome'] = operatingIncome
    ##income_statement['operatingIncomeRatio'] = operatingIncome / revenue
    income_statement['totalOtherIncomeExpensesNet'] =totalOtherIncomeExpensesNet
    income_statement['incomeBeforeTax'] = incomeBeforeTax
    income_statement['incomeBeforeTaxRatio'] = incomeBeforeTax / revenue
    ##income_statement['incomeTaxExpense'] = incomeTaxExpense
    income_statement['netIncome'] = netIncome
    income_statement['netIncomeRatio'] = netIncome / revenue
    income_statement['eps'] = eps
    income_statement['epsdiluted'] = epsdiluted
    income_statement['weightedAverageShsOut'] = weightedAverageShsOut
    income_statement['weightedAverageShsOutDil'] = weightedAverageShsOutDil
    '''
    income_statement['link'] = 'w'
    income_statement['finalLink'] = 'w'
    '''
    return income_statement     



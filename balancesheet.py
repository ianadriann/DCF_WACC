


def date_bs_annual(input1, B_S_start, I_S_start, ticker_code):
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
    date = I_S_start['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory'][year]['endDate']['fmt']
    reportedCurrency = I_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOperatingExpense'][input2]['currencyCode']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashAndCashEquivalents'] == []:
        cashAndCashEquivalents = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashAndCashEquivalents'][input2] == None:
        cashAndCashEquivalents = 0
    else:
        cashAndCashEquivalents = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashAndCashEquivalents'][input2]['reportedValue']['raw']


    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherShortTermInvestments'] == []:
        shortTermInvestments = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherShortTermInvestments'][input2] == None:
        shortTermInvestments = 0
    else:
        shortTermInvestments = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherShortTermInvestments'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashCashEquivalentsAndShortTermInvestments'] == []:
        cashAndShortTermInvestments = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashCashEquivalentsAndShortTermInvestments'][input2] == None:
        cashAndShortTermInvestments = 0
    else:
        cashAndShortTermInvestments = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCashCashEquivalentsAndShortTermInvestments'][input2]['reportedValue']['raw']

    if B_S_start['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements'] == []:
        netReceivables = 0
    elif B_S_start['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements'][year] == None:
        netReceivables = 0
    else:
        netReceivables = B_S_start['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements'][year]['netReceivables']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInventory'] == []:
        inventory = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInventory'][input2] == None:
        inventory = 0
    else:
        inventory = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInventory'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentAssets'] == []:
        otherCurrentAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentAssets'][input2] == None:
        otherCurrentAssets = 0
    else:
        otherCurrentAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentAssets'] == []:
        totalCurrentAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentAssets'][input2] == None:
        totalCurrentAssets = 0
    else:
        totalCurrentAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetPPE'] == []:
        propertyPlantEquipmentNet = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetPPE'][input2] == None:
        propertyPlantEquipmentNet = 0
    else:
        propertyPlantEquipmentNet = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetPPE'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwill'] == []:
        goodwill = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwill'][input2] == None:
        goodwill = 0
    else:
        goodwill = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwill'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherIntangibleAssets'] == []:
        intangibleAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherIntangibleAssets'][input2] == None:
        intangibleAssets = 0
    else:
        intangibleAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherIntangibleAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwillAndOtherIntangibleAssets'] == []:
        goodwillAndIntangibleAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwillAndOtherIntangibleAssets'][input2] == None:
        goodwillAndIntangibleAssets = 0
    else:
        goodwillAndIntangibleAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGoodwillAndOtherIntangibleAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInvestmentsAndAdvances'] == []:
        longTermInvestments = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInvestmentsAndAdvances'][input2] == None:
        longTermInvestments = 0
    else:
        longTermInvestments = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualInvestmentsAndAdvances'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesAssets'] == []:
        taxAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesAssets'][input2] == None:
        taxAssets = 0
    else:
        taxAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherNonCurrentAssets'] == []:
        otherNonCurrentAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherNonCurrentAssets'][input2] == None:
        otherNonCurrentAssets = 0
    else:
        otherNonCurrentAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherNonCurrentAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentAssets'] == []:
        totalNonCurrentAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentAssets'][input2] == None:
        totalNonCurrentAssets = 0
    else:
        totalNonCurrentAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredAssets'] == []:
        otherAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredAssets'][input2] == None:
        otherAssets = 0
    else:
        otherAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalAssets'] == []:
        totalAssets = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalAssets'][input2] == None:
        totalAssets = 0
    else:
        totalAssets = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalAssets'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualAccountsPayable'] == []:
        accountPayables = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualAccountsPayable'][input2] == None:
        accountPayables = 0
    else:
        accountPayables = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualAccountsPayable'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDebtAndCapitalLeaseObligation'] == []:
        shortTermDebt = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDebtAndCapitalLeaseObligation'][input2] == None:
        shortTermDebt = 0
    else:
        shortTermDebt = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDebtAndCapitalLeaseObligation'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualIncomeTaxPayable'] == []:
        taxPayables = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualIncomeTaxPayable'][input2] == None:
        taxPayables = 0
    else:
        taxPayables = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualIncomeTaxPayable'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredRevenue'] == []:
        deferredRevenue = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredRevenue'][input2] == None:
        deferredRevenue = 0
    else:
        deferredRevenue = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentDeferredRevenue'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentLiabilities'] == []:
        otherCurrentLiabilities = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentLiabilities'][input2] == None:
        otherCurrentLiabilities = 0
    else:
        otherCurrentLiabilities = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualOtherCurrentLiabilities'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentLiabilities'] == []:
        totalCurrentLiabilities = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentLiabilities'][input2] == None:
        totalCurrentLiabilities = 0
    else:
        totalCurrentLiabilities = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCurrentLiabilities'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualLongTermDebt'] == []:
        longTermDebt = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualLongTermDebt'][input2] == None:
        longTermDebt = 0
    else:
        longTermDebt = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualLongTermDebt'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredRevenue'] == []:
        deferredRevenueNonCurrent = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredRevenue'][input2] == None:
        deferredRevenueNonCurrent = 0
    else:
        deferredRevenueNonCurrent = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredRevenue'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesLiabilities'] == []:
        deferredTaxLiabilitiesNonCurrent = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesLiabilities'][input2] == None:
        deferredTaxLiabilitiesNonCurrent = 0
    else:
        deferredTaxLiabilitiesNonCurrent = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNonCurrentDeferredTaxesLiabilities'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentLiabilitiesNetMinorityInterest'] == []:
        totalNonCurrentLiabilities = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentLiabilitiesNetMinorityInterest'][input2] == None:
        totalNonCurrentLiabilities = 0
    else:
        totalNonCurrentLiabilities = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalNonCurrentLiabilitiesNetMinorityInterest'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCapitalLeaseObligations'] == []:
        capitalLeaseObligations = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCapitalLeaseObligations'][input2] == None:
        capitalLeaseObligations = 0
    else:
        capitalLeaseObligations = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCapitalLeaseObligations'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalLiabilitiesNetMinorityInterest'] == []:
        totalLiabilities = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalLiabilitiesNetMinorityInterest'][input2] == None:
        totalLiabilities = 0
    else:
        totalLiabilities = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalLiabilitiesNetMinorityInterest'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualPreferredStock'] == []:
        preferredStock = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualPreferredStock'][input2] == None:
        preferredStock = 0
    else:
        preferredStock = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualPreferredStock'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCommonStock'] == []:
        commonStock = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCommonStock'][input2] == None:
        commonStock = 0
    else:
        commonStock = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualCommonStock'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualRetainedEarnings'] == []:
        retainedEarnings = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualRetainedEarnings'][input2] == None:
        retainedEarnings = 0
    else:
        retainedEarnings = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualRetainedEarnings'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGainsLossesNotAffectingRetainedEarnings'] == []:
        accumulatedOtherComprehensiveIncomeLoss = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGainsLossesNotAffectingRetainedEarnings'][input2] == None:
        accumulatedOtherComprehensiveIncomeLoss = 0
    else:
        accumulatedOtherComprehensiveIncomeLoss = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualGainsLossesNotAffectingRetainedEarnings'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTreasuryStock'] == []:
        othertotalStockholdersEquity = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTreasuryStock'][input2] == None:
        othertotalStockholdersEquity = 0
    else:
        othertotalStockholdersEquity = -B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTreasuryStock'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualStockholdersEquity'] == []:
        totalStockholdersEquity = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualStockholdersEquity'][input2] == None:
        totalStockholdersEquity = 0
    else:
        totalStockholdersEquity = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualStockholdersEquity'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualMinorityInterest'] == []:
        minorityInterest = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualMinorityInterest'][input2] == None:
        minorityInterest = 0
    else:
        minorityInterest = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualMinorityInterest'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalEquityGrossMinorityInterest'] == []:
        totalEquity = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalEquityGrossMinorityInterest'][input2] == None:
        totalEquity = 0
    else:
        totalEquity = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalEquityGrossMinorityInterest'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalDebt'] == []:
        totalDebt = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalDebt'][input2] == None:
        totalDebt = 0
    else:
        totalDebt = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualTotalDebt'][input2]['reportedValue']['raw']

    if B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetDebt'] == []:
        netDebt = 0
    elif B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetDebt'][input2] == None:
        netDebt = 0
    else:
        netDebt = B_S_start['QuoteTimeSeriesStore']['timeSeries']['annualNetDebt'][input2]['reportedValue']['raw']

    #======================
    balance_sheet_statement = {}
    ''' 
    balance_sheet_statement['date'] = date 
    balance_sheet_statement['symbol'] = ticker_code
    balance_sheet_statement['reportedCurrency'] = reportedCurrency
    balance_sheet_statement['cik'] = 'cik'
    balance_sheet_statement['fillingDate'] = 'fillingDate'
    balance_sheet_statement['acceptedDate'] = 'xxxxxx'
    balance_sheet_statement['calendarYear'] = date
    balance_sheet_statement['period'] = 'FY'
    '''
    balance_sheet_statement['cashAndCashEquivalents'] =  cashAndCashEquivalents
    balance_sheet_statement['shortTermInvestments'] = shortTermInvestments
    balance_sheet_statement['cashAndShortTermInvestments'] = cashAndShortTermInvestments
    balance_sheet_statement['netReceivables'] = netReceivables
    balance_sheet_statement['inventory'] = inventory
    balance_sheet_statement['otherCurrentAssets'] = otherCurrentAssets
    balance_sheet_statement['totalCurrentAssets'] = totalCurrentAssets
    balance_sheet_statement['propertyPlantEquipmentNet'] = propertyPlantEquipmentNet
    balance_sheet_statement['goodwill'] = goodwill
    balance_sheet_statement['intangibleAssets'] = intangibleAssets
    balance_sheet_statement['goodwillAndIntangibleAssets'] = goodwillAndIntangibleAssets
    balance_sheet_statement['longTermInvestments'] = longTermInvestments
    balance_sheet_statement['taxAssets'] = taxAssets
    balance_sheet_statement['otherNonCurrentAssets'] = otherNonCurrentAssets
    balance_sheet_statement['totalNonCurrentAssets'] = totalNonCurrentAssets
    balance_sheet_statement['otherAssets'] = otherAssets
    balance_sheet_statement['totalAssets'] = totalAssets
    balance_sheet_statement['accountPayables'] = accountPayables
    balance_sheet_statement['shortTermDebt'] = shortTermDebt
    balance_sheet_statement['taxPayables'] = taxPayables
    balance_sheet_statement['deferredRevenue'] = deferredRevenue
    balance_sheet_statement['otherCurrentLiabilities'] = otherCurrentLiabilities
    balance_sheet_statement['totalCurrentLiabilities'] = totalCurrentLiabilities
    balance_sheet_statement['longTermDebt'] = longTermDebt
    balance_sheet_statement['deferredRevenueNonCurrent'] = deferredRevenueNonCurrent
    balance_sheet_statement['deferredTaxLiabilitiesNonCurrent'] = deferredTaxLiabilitiesNonCurrent
    balance_sheet_statement['otherNonCurrentLiabilities'] = totalNonCurrentLiabilities - longTermDebt
    balance_sheet_statement['totalNonCurrentLiabilities'] = totalNonCurrentLiabilities
    balance_sheet_statement['otherLiabilities'] = 0
    balance_sheet_statement['capitalLeaseObligations'] = capitalLeaseObligations
    balance_sheet_statement['totalLiabilities'] = totalLiabilities
    balance_sheet_statement['preferredStock'] = preferredStock
    balance_sheet_statement['commonStock'] = commonStock
    balance_sheet_statement['retainedEarnings'] = retainedEarnings
    balance_sheet_statement['accumulatedOtherComprehensiveIncomeLoss'] = accumulatedOtherComprehensiveIncomeLoss
    balance_sheet_statement['othertotalStockholdersEquity'] = othertotalStockholdersEquity
    balance_sheet_statement['totalStockholdersEquity'] = totalStockholdersEquity
    balance_sheet_statement['totalLiabilitiesAndStockholdersEquity'] = totalLiabilities + totalStockholdersEquity
    balance_sheet_statement['minorityInterest'] = minorityInterest
    balance_sheet_statement['totalEquity'] = totalEquity
    balance_sheet_statement['totalLiabilitiesAndTotalEquity'] = totalLiabilities + totalEquity
    balance_sheet_statement['totalInvestments'] = 0
    balance_sheet_statement['totalDebt'] = totalDebt
    balance_sheet_statement['netDebt'] = netDebt
    '''
    balance_sheet_statement['link'] = 'w'
    balance_sheet_statement['finallink'] = 'w'
    '''
    return balance_sheet_statement
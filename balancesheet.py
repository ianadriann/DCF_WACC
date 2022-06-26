def date_bs_annual(input1, I_S_totalOtherIncomeExpensesNet, B_S, I_S, ticker_code):
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
    date = I_S_totalOtherIncomeExpensesNet[year]['endDate']['fmt']
    reportedCurrency = I_S['annualOperatingExpense'][input2]['currencyCode']

    if B_S['annualCashAndCashEquivalents'] == []:
        cashAndCashEquivalents = 0
    elif B_S['annualCashAndCashEquivalents'][input2] == None:
        cashAndCashEquivalents = 0
    else:
        cashAndCashEquivalents = B_S['annualCashAndCashEquivalents'][input2]['reportedValue']['raw']


    if B_S['annualOtherShortTermInvestments'] == []:
        shortTermInvestments = 0
    elif B_S['annualOtherShortTermInvestments'][input2] == None:
        shortTermInvestments = 0
    else:
        shortTermInvestments = B_S['annualOtherShortTermInvestments'][input2]['reportedValue']['raw']

    if B_S['annualCashCashEquivalentsAndShortTermInvestments'] == []:
        cashAndShortTermInvestments = 0
    elif B_S['annualCashCashEquivalentsAndShortTermInvestments'][input2] == None:
        cashAndShortTermInvestments = 0
    else:
        cashAndShortTermInvestments = B_S['annualCashCashEquivalentsAndShortTermInvestments'][input2]['reportedValue']['raw']

    if B_S['annualReceivables'] == []:
        netReceivables = 0
    elif B_S['annualReceivables'][input2] == None:
        netReceivables = 0
    else:
        netReceivables = B_S['annualReceivables'][input2]['reportedValue']['raw']

    if B_S['annualInventory'] == []:
        inventory = 0
    elif B_S['annualInventory'][input2] == None:
        inventory = 0
    else:
        inventory = B_S['annualInventory'][input2]['reportedValue']['raw']

    if B_S['annualOtherCurrentAssets'] == []:
        otherCurrentAssets = 0
    elif B_S['annualOtherCurrentAssets'][input2] == None:
        otherCurrentAssets = 0
    else:
        otherCurrentAssets = B_S['annualOtherCurrentAssets'][input2]['reportedValue']['raw']

    if B_S['annualCurrentAssets'] == []:
        totalCurrentAssets = 0
    elif B_S['annualCurrentAssets'][input2] == None:
        totalCurrentAssets = 0
    else:
        totalCurrentAssets = B_S['annualCurrentAssets'][input2]['reportedValue']['raw']

    if B_S['annualNetPPE'] == []:
        propertyPlantEquipmentNet = 0
    elif B_S['annualNetPPE'][input2] == None:
        propertyPlantEquipmentNet = 0
    else:
        propertyPlantEquipmentNet = B_S['annualNetPPE'][input2]['reportedValue']['raw']

    if B_S['annualGoodwill'] == []:
        goodwill = 0
    elif B_S['annualGoodwill'][input2] == None:
        goodwill = 0
    else:
        goodwill = B_S['annualGoodwill'][input2]['reportedValue']['raw']

    if B_S['annualOtherIntangibleAssets'] == []:
        intangibleAssets = 0
    elif B_S['annualOtherIntangibleAssets'][input2] == None:
        intangibleAssets = 0
    else:
        intangibleAssets = B_S['annualOtherIntangibleAssets'][input2]['reportedValue']['raw']

    if B_S['annualGoodwillAndOtherIntangibleAssets'] == []:
        goodwillAndIntangibleAssets = 0
    elif B_S['annualGoodwillAndOtherIntangibleAssets'][input2] == None:
        goodwillAndIntangibleAssets = 0
    else:
        goodwillAndIntangibleAssets = B_S['annualGoodwillAndOtherIntangibleAssets'][input2]['reportedValue']['raw']

    if B_S['annualInvestmentsAndAdvances'] == []:
        longTermInvestments = 0
    elif B_S['annualInvestmentsAndAdvances'][input2] == None:
        longTermInvestments = 0
    else:
        longTermInvestments = B_S['annualInvestmentsAndAdvances'][input2]['reportedValue']['raw']

    if B_S['annualNonCurrentDeferredTaxesAssets'] == []:
        taxAssets = 0
    elif B_S['annualNonCurrentDeferredTaxesAssets'][input2] == None:
        taxAssets = 0
    else:
        taxAssets = B_S['annualNonCurrentDeferredTaxesAssets'][input2]['reportedValue']['raw']

    if B_S['annualOtherNonCurrentAssets'] == []:
        otherNonCurrentAssets = 0
    elif B_S['annualOtherNonCurrentAssets'][input2] == None:
        otherNonCurrentAssets = 0
    else:
        otherNonCurrentAssets = B_S['annualOtherNonCurrentAssets'][input2]['reportedValue']['raw']

    if B_S['annualTotalNonCurrentAssets'] == []:
        totalNonCurrentAssets = 0
    elif B_S['annualTotalNonCurrentAssets'][input2] == None:
        totalNonCurrentAssets = 0
    else:
        totalNonCurrentAssets = B_S['annualTotalNonCurrentAssets'][input2]['reportedValue']['raw']

    if B_S['annualCurrentDeferredAssets'] == []:
        otherAssets = 0
    elif B_S['annualCurrentDeferredAssets'][input2] == None:
        otherAssets = 0
    else:
        otherAssets = B_S['annualCurrentDeferredAssets'][input2]['reportedValue']['raw']

    if B_S['annualTotalAssets'] == []:
        totalAssets = 0
    elif B_S['annualTotalAssets'][input2] == None:
        totalAssets = 0
    else:
        totalAssets = B_S['annualTotalAssets'][input2]['reportedValue']['raw']

    if B_S['annualAccountsPayable'] == []:
        accountPayables = 0
    elif B_S['annualAccountsPayable'][input2] == None:
        accountPayables = 0
    else:
        accountPayables = B_S['annualAccountsPayable'][input2]['reportedValue']['raw']

    if B_S['annualCurrentDebtAndCapitalLeaseObligation'] == []:
        shortTermDebt = 0
    elif B_S['annualCurrentDebtAndCapitalLeaseObligation'][input2] == None:
        shortTermDebt = 0
    else:
        shortTermDebt = B_S['annualCurrentDebtAndCapitalLeaseObligation'][input2]['reportedValue']['raw']

    if B_S['annualIncomeTaxPayable'] == []:
        taxPayables = 0
    elif B_S['annualIncomeTaxPayable'][input2] == None:
        taxPayables = 0
    else:
        taxPayables = B_S['annualIncomeTaxPayable'][input2]['reportedValue']['raw']

    if B_S['annualCurrentDeferredRevenue'] == []:
        deferredRevenue = 0
    elif B_S['annualCurrentDeferredRevenue'][input2] == None:
        deferredRevenue = 0
    else:
        deferredRevenue = B_S['annualCurrentDeferredRevenue'][input2]['reportedValue']['raw']

    if B_S['annualOtherCurrentLiabilities'] == []:
        otherCurrentLiabilities = 0
    elif B_S['annualOtherCurrentLiabilities'][input2] == None:
        otherCurrentLiabilities = 0
    else:
        otherCurrentLiabilities = B_S['annualOtherCurrentLiabilities'][input2]['reportedValue']['raw']

    if B_S['annualCurrentLiabilities'] == []:
        totalCurrentLiabilities = 0
    elif B_S['annualCurrentLiabilities'][input2] == None:
        totalCurrentLiabilities = 0
    else:
        totalCurrentLiabilities = B_S['annualCurrentLiabilities'][input2]['reportedValue']['raw']

    if B_S['annualLongTermDebt'] == []:
        longTermDebt = 0
    elif B_S['annualLongTermDebt'][input2] == None:
        longTermDebt = 0
    else:
        longTermDebt = B_S['annualLongTermDebt'][input2]['reportedValue']['raw']

    if B_S['annualNonCurrentDeferredRevenue'] == []:
        deferredRevenueNonCurrent = 0
    elif B_S['annualNonCurrentDeferredRevenue'][input2] == None:
        deferredRevenueNonCurrent = 0
    else:
        deferredRevenueNonCurrent = B_S['annualNonCurrentDeferredRevenue'][input2]['reportedValue']['raw']

    if B_S['annualNonCurrentDeferredTaxesLiabilities'] == []:
        deferredTaxLiabilitiesNonCurrent = 0
    elif B_S['annualNonCurrentDeferredTaxesLiabilities'][input2] == None:
        deferredTaxLiabilitiesNonCurrent = 0
    else:
        deferredTaxLiabilitiesNonCurrent = B_S['annualNonCurrentDeferredTaxesLiabilities'][input2]['reportedValue']['raw']

    if B_S['annualTotalNonCurrentLiabilitiesNetMinorityInterest'] == []:
        totalNonCurrentLiabilities = 0
    elif B_S['annualTotalNonCurrentLiabilitiesNetMinorityInterest'][input2] == None:
        totalNonCurrentLiabilities = 0
    else:
        totalNonCurrentLiabilities = B_S['annualTotalNonCurrentLiabilitiesNetMinorityInterest'][input2]['reportedValue']['raw']

    if B_S['annualCapitalLeaseObligations'] == []:
        capitalLeaseObligations = 0
    elif B_S['annualCapitalLeaseObligations'][input2] == None:
        capitalLeaseObligations = 0
    else:
        capitalLeaseObligations = B_S['annualCapitalLeaseObligations'][input2]['reportedValue']['raw']

    if B_S['annualTotalLiabilitiesNetMinorityInterest'] == []:
        totalLiabilities = 0
    elif B_S['annualTotalLiabilitiesNetMinorityInterest'][input2] == None:
        totalLiabilities = 0
    else:
        totalLiabilities = B_S['annualTotalLiabilitiesNetMinorityInterest'][input2]['reportedValue']['raw']

    if B_S['annualPreferredStock'] == []:
        preferredStock = 0
    elif B_S['annualPreferredStock'][input2] == None:
        preferredStock = 0
    else:
        preferredStock = B_S['annualPreferredStock'][input2]['reportedValue']['raw']

    if B_S['annualCommonStock'] == []:
        commonStock = 0
    elif B_S['annualCommonStock'][input2] == None:
        commonStock = 0
    else:
        commonStock = B_S['annualCommonStock'][input2]['reportedValue']['raw']

    if B_S['annualRetainedEarnings'] == []:
        retainedEarnings = 0
    elif B_S['annualRetainedEarnings'][input2] == None:
        retainedEarnings = 0
    else:
        retainedEarnings = B_S['annualRetainedEarnings'][input2]['reportedValue']['raw']

    if B_S['annualGainsLossesNotAffectingRetainedEarnings'] == []:
        accumulatedOtherComprehensiveIncomeLoss = 0
    elif B_S['annualGainsLossesNotAffectingRetainedEarnings'][input2] == None:
        accumulatedOtherComprehensiveIncomeLoss = 0
    else:
        accumulatedOtherComprehensiveIncomeLoss = B_S['annualGainsLossesNotAffectingRetainedEarnings'][input2]['reportedValue']['raw']

    if B_S['annualTreasuryStock'] == []:
        othertotalStockholdersEquity = 0
    elif B_S['annualTreasuryStock'][input2] == None:
        othertotalStockholdersEquity = 0
    else:
        othertotalStockholdersEquity = -B_S['annualTreasuryStock'][input2]['reportedValue']['raw']

    if B_S['annualStockholdersEquity'] == []:
        totalStockholdersEquity = 0
    elif B_S['annualStockholdersEquity'][input2] == None:
        totalStockholdersEquity = 0
    else:
        totalStockholdersEquity = B_S['annualStockholdersEquity'][input2]['reportedValue']['raw']

    if B_S['annualMinorityInterest'] == []:
        minorityInterest = 0
    elif B_S['annualMinorityInterest'][input2] == None:
        minorityInterest = 0
    else:
        minorityInterest = B_S['annualMinorityInterest'][input2]['reportedValue']['raw']

    if B_S['annualTotalEquityGrossMinorityInterest'] == []:
        totalEquity = 0
    elif B_S['annualTotalEquityGrossMinorityInterest'][input2] == None:
        totalEquity = 0
    else:
        totalEquity = B_S['annualTotalEquityGrossMinorityInterest'][input2]['reportedValue']['raw']

    if B_S['annualTotalDebt'] == []:
        totalDebt = 0
    elif B_S['annualTotalDebt'][input2] == None:
        totalDebt = 0
    else:
        totalDebt = B_S['annualTotalDebt'][input2]['reportedValue']['raw']

    if B_S['annualNetDebt'] == []:
        netDebt = 0
    elif B_S['annualNetDebt'][input2] == None:
        netDebt = 0
    else:
        netDebt = B_S['annualNetDebt'][input2]['reportedValue']['raw']

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
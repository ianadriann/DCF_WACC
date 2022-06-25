def freecashflow(income_statement, balance_sheet):
    #model free cash flow
    CF_forecast = {}
    CF_forecast['next_year'] = {}
    CF_forecast['next_year']['netIncome'] = income_statement['next_year']['netIncome']
    CF_forecast['next_year']['inc_depreciation'] = income_statement['next_year']['depreciationAndAmortization'] - income_statement['current_year']['depreciationAndAmortization']
    CF_forecast['next_year']['inc_receivables'] = balance_sheet['next_year']['netReceivables'] - balance_sheet['current_year']['netReceivables']
    CF_forecast['next_year']['inc_inventory'] = balance_sheet['next_year']['inventory'] - balance_sheet['current_year']['inventory']
    CF_forecast['next_year']['inc_payables'] = balance_sheet['next_year']['accountPayables'] - balance_sheet['current_year']['accountPayables']
    CF_forecast['next_year']['CF_operations'] = CF_forecast['next_year']['netIncome'] + CF_forecast['next_year']['inc_depreciation'] + (CF_forecast['next_year']['inc_receivables'] * -1) + (CF_forecast['next_year']['inc_inventory'] *-1) + CF_forecast['next_year']['inc_payables']
    CF_forecast['next_year']['CAPEX'] = balance_sheet['next_year']['propertyPlantEquipmentNet'] - balance_sheet['current_year']['propertyPlantEquipmentNet'] + income_statement['next_year']['depreciationAndAmortization']
    CF_forecast['next_year']['FCF'] = CF_forecast['next_year']['CAPEX'] + CF_forecast['next_year']['CF_operations']


    #model free cash flow 5 years
    CF_forecast['next_2_year'] = {}
    CF_forecast['next_2_year']['netIncome'] = income_statement['next_2_year']['netIncome']
    CF_forecast['next_2_year']['inc_depreciation'] = income_statement['next_2_year']['depreciationAndAmortization'] - income_statement['next_year']['depreciationAndAmortization']
    CF_forecast['next_2_year']['inc_receivables'] = balance_sheet['next_2_year']['netReceivables'] - balance_sheet['next_year']['netReceivables']
    CF_forecast['next_2_year']['inc_inventory'] = balance_sheet['next_2_year']['inventory'] - balance_sheet['next_year']['inventory']
    CF_forecast['next_2_year']['inc_payables'] = balance_sheet['next_2_year']['accountPayables'] - balance_sheet['next_year']['accountPayables']
    CF_forecast['next_2_year']['CF_operations'] = CF_forecast['next_2_year']['netIncome'] + CF_forecast['next_2_year']['inc_depreciation'] + (CF_forecast['next_2_year']['inc_receivables'] * -1) + (CF_forecast['next_2_year']['inc_inventory'] *-1) + CF_forecast['next_2_year']['inc_payables']
    CF_forecast['next_2_year']['CAPEX'] = balance_sheet['next_2_year']['propertyPlantEquipmentNet'] - balance_sheet['next_year']['propertyPlantEquipmentNet'] + income_statement['next_2_year']['depreciationAndAmortization']
    CF_forecast['next_2_year']['FCF'] = CF_forecast['next_2_year']['CAPEX'] + CF_forecast['next_2_year']['CF_operations']


    CF_forecast['next_3_year'] = {}
    CF_forecast['next_3_year']['netIncome'] = income_statement['next_3_year']['netIncome']
    CF_forecast['next_3_year']['inc_depreciation'] = income_statement['next_3_year']['depreciationAndAmortization'] - income_statement['next_2_year']['depreciationAndAmortization']
    CF_forecast['next_3_year']['inc_receivables'] = balance_sheet['next_3_year']['netReceivables'] - balance_sheet['next_2_year']['netReceivables']
    CF_forecast['next_3_year']['inc_inventory'] = balance_sheet['next_3_year']['inventory'] - balance_sheet['next_2_year']['inventory']
    CF_forecast['next_3_year']['inc_payables'] = balance_sheet['next_3_year']['accountPayables'] - balance_sheet['next_2_year']['accountPayables']
    CF_forecast['next_3_year']['CF_operations'] = CF_forecast['next_3_year']['netIncome'] + CF_forecast['next_3_year']['inc_depreciation'] + (CF_forecast['next_3_year']['inc_receivables'] * -1) + (CF_forecast['next_3_year']['inc_inventory'] *-1) + CF_forecast['next_3_year']['inc_payables']
    CF_forecast['next_3_year']['CAPEX'] = balance_sheet['next_3_year']['propertyPlantEquipmentNet'] - balance_sheet['next_2_year']['propertyPlantEquipmentNet'] + income_statement['next_3_year']['depreciationAndAmortization']
    CF_forecast['next_3_year']['FCF'] = CF_forecast['next_3_year']['CAPEX'] + CF_forecast['next_3_year']['CF_operations']


    CF_forecast['next_4_year'] = {}
    CF_forecast['next_4_year']['netIncome'] = income_statement['next_4_year']['netIncome']
    CF_forecast['next_4_year']['inc_depreciation'] = income_statement['next_4_year']['depreciationAndAmortization'] - income_statement['next_3_year']['depreciationAndAmortization']
    CF_forecast['next_4_year']['inc_receivables'] = balance_sheet['next_4_year']['netReceivables'] - balance_sheet['next_3_year']['netReceivables']
    CF_forecast['next_4_year']['inc_inventory'] = balance_sheet['next_4_year']['inventory'] - balance_sheet['next_3_year']['inventory']
    CF_forecast['next_4_year']['inc_payables'] = balance_sheet['next_4_year']['accountPayables'] - balance_sheet['next_3_year']['accountPayables']
    CF_forecast['next_4_year']['CF_operations'] = CF_forecast['next_4_year']['netIncome'] + CF_forecast['next_4_year']['inc_depreciation'] + (CF_forecast['next_4_year']['inc_receivables'] * -1) + (CF_forecast['next_4_year']['inc_inventory'] *-1) + CF_forecast['next_4_year']['inc_payables']
    CF_forecast['next_4_year']['CAPEX'] = balance_sheet['next_4_year']['propertyPlantEquipmentNet'] - balance_sheet['next_3_year']['propertyPlantEquipmentNet'] + income_statement['next_4_year']['depreciationAndAmortization']
    CF_forecast['next_4_year']['FCF'] = CF_forecast['next_4_year']['CAPEX'] + CF_forecast['next_4_year']['CF_operations']

    CF_forecast['next_5_year'] = {}
    CF_forecast['next_5_year']['netIncome'] = income_statement['next_5_year']['netIncome']
    CF_forecast['next_5_year']['inc_depreciation'] = income_statement['next_5_year']['depreciationAndAmortization'] - income_statement['next_4_year']['depreciationAndAmortization']
    CF_forecast['next_5_year']['inc_receivables'] = balance_sheet['next_5_year']['netReceivables'] - balance_sheet['next_4_year']['netReceivables']
    CF_forecast['next_5_year']['inc_inventory'] = balance_sheet['next_5_year']['inventory'] - balance_sheet['next_4_year']['inventory']
    CF_forecast['next_5_year']['inc_payables'] = balance_sheet['next_5_year']['accountPayables'] - balance_sheet['next_4_year']['accountPayables']
    CF_forecast['next_5_year']['CF_operations'] = CF_forecast['next_5_year']['netIncome'] + CF_forecast['next_5_year']['inc_depreciation'] + (CF_forecast['next_5_year']['inc_receivables'] * -1) + (CF_forecast['next_5_year']['inc_inventory'] *-1) + CF_forecast['next_5_year']['inc_payables']
    CF_forecast['next_5_year']['CAPEX'] = balance_sheet['next_5_year']['propertyPlantEquipmentNet'] - balance_sheet['next_4_year']['propertyPlantEquipmentNet'] + income_statement['next_5_year']['depreciationAndAmortization']
    CF_forecast['next_5_year']['FCF'] = CF_forecast['next_5_year']['CAPEX'] + CF_forecast['next_5_year']['CF_operations']
    return CF_forecast
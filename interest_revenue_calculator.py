initialCapital = 10000  # initial capital put into bank deposit
percent = 0.05  # annual interest rate
maxTimeYears = 5  # investment period
finalValue = initialCapital  # amount after capitalization of interest
year = 0  # represent the year of investment
capital_gains_tax = 0.19  # Poland tax based on capital gains

while year < 5:
    finalValue = finalValue * (1 + percent)
    profit_not_include_tax = finalValue - initialCapital
    profit_include_tax = finalValue - (profit_not_include_tax * capital_gains_tax)
    year += 1
    print(f'Final Value after {year} year is {finalValue: .2f} zł, whole profit is {profit_not_include_tax: .2f} zł, total amount after including capital gain tax is {profit_include_tax: .2f} zł.')




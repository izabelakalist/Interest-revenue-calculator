initialCapital = 10000  # initial capital put into bank deposit
percent = 0.05  # annual interest rate
maxTimeYears = 5  # investment period
finalValue = initialCapital  # amount after capitalization of interest
year = 1  # represent the year of investment

while year < 5:
    finalValue = finalValue * (1 + percent)
    print(year, round(finalValue))
    year += 1

print("Final value after", year, "years is", round(finalValue, 2), "zł")


# Implement a function that receives 2 lists of strings - dates and stocks.
# Dates contain various dates represented as string in format dd-mm-yy,
# and stocks list contains tickers of stocks that fell more than 5% in the corresponding date.
#
# You should return 2 dictionaries - the first one maps dates to list of stocks that fell more than 5% in that date,
# the second one maps stocks to list of dates in which they fell.

# For example, for the input:
dates = ["11-05-22", "12-05-22", "13-05-22", "12-05-22", "11-05-22", "11-05-22"]
stocks = ["TSLA", "TSLA", "AAPL", "MSFT", "AAPL", "IBM"]

# Your functions should return the following 2 dictionaries:
# {
#     "11-05-22": ["TSLA", "AAPL", "IBM"],
#     "12-05-22": ["TSLA", "MSFT", ],
#     "13-05-22": ["AAPL"]
# }
#
# {"TSLA": ["11-05-22", "12-05-22"],
#  "AAPL": ["13-05-22", "11-05-22"],
#  "MSFT": ["12-05-22"],
#  "IBM": ["11-05-22"]}

# def dict_creator(dates: list[str], stocks: list[str]) -> tuple:
#     dates_to_stocks = {date: [stock for i, stock in enumerate(stocks) if dates[i] == date] for date in dates}
#     stocks_to_dates = {stock: [date for i, date in enumerate(dates) if stocks[i] == stock] for stock in stocks}
#     return dates_to_stocks, stocks_to_dates
#
# print(dict_creator(dates, stocks))

def dict_creator_2(dates: list[str], stocks: list[str]) -> tuple:
    dates_to_stocks = dict()
    stocks_to_dates = dict()
    for date, stock in zip(dates, stocks):
        if date not in dates_to_stocks:
            dates_to_stocks[date] = []
        dates_to_stocks[date].append(stock)
        if stock not in stocks_to_dates:
            stocks_to_dates[stock] = []
        stocks_to_dates[stock].append(date)
    return dates_to_stocks, stocks_to_dates

print(dict_creator_2(dates, stocks))


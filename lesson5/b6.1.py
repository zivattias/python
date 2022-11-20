# Implement a dictionary to store stocks data. Your dictionary should allow searching stocks by ticker.
# Data you should be able to store in your dictionary:

# Ticker
# Company name
# Employees number
# Address
# CEO name
# Stock prices data by date that includes: open price, close price, volume

# For example:
# company: Tesla
# ticker: TSLA
# employees num: 5000
# address: California
# CEO: Elon Musk
# stocks data (per date):
#  ...
#  14.11.2021: open price 1001.5, close price: 1020, volume: 50000000
#  15.11.2021: open price: 1067.7, close price: 1045.5, volume: 45000345
#  ...
import pprint

company_profiles: dict = {
    "TSLA":
        {
            "Company Name": "Tesla",
            "Ticker": "TSLA",
            "# of Employees": 50_000,
            "Address": "Palo Alto",
            "CEO": "Elon Musk",
            "Stock Data": {
                "19/11/2022":
                    {
                        "Open Price (USD)": 2_000.2,
                        "Closing Price (USD)": 2_200.2,
                        "Volume": 5_000_000
                    },
                "20/11/2022":
                    {
                        "Open Price (USD)": 2_200.2,
                        "Closing Price (USD)": 2_400.2,
                        "Volume": 6_000_000
                    }
            }
        },
    "AAPL":
        {
            "Company Name": "Apple",
            "Ticker": "AAPL",
            "# of Employees": 70_000,
            "Address": "Silicon Valley",
            "CEO": "Tim Cooks",
            "Stock Data": {
                "19/11/2022":
                    {
                        "Open Price (USD)": 1_000.2,
                        "Closing Price (USD)": 1_200.2,
                        "Volume": 5_000_000
                    },
                "20/11/2022":
                    {
                        "Open Price (USD)": 1_200.2,
                        "Closing Price (USD)": 1_400.2,
                        "Volume": 6_000_000
                    }
            }
        }
}

pprint.pprint(company_profiles['TSLA']['Stock Data']['19/11/2022']['Open Price (USD)'])
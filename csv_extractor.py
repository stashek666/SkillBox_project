import pandas as pd

# Url of site where we can download csv history data for free
URL = "https://www.cryptodatadownload.com/cdd/Binance_{symbol}USDT_d.csv"
FILENAME = 'Binance_{symbol}USDT_d.csv'

def get_historical_data(symbol: str = "BTC") -> pd.DataFrame:
    try:
        file = FILENAME.format(symbol=symbol)
        df = pd.read_csv(file, delimiter=",", skiprows=[0], header=0, parse_dates=[1])
    except FileNotFoundError:
        url = URL.format(symbol=symbol)
        df = pd.read_csv(url, delimiter=",", skiprows=[0], header=0, parse_dates=[1])
        # We delete the columns we don't need. Using of date is possible
        # (e.x. increasing weights for last time) but for now we leave this idea
    df.set_index(['Date'], inplace=True)
    return df.drop(['Unix', 'Symbol'], axis=1, inplace=False)

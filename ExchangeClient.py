from pybit.unified_trading import HTTP, WebSocket
#from secret_data import BYBIT_KEY, BYBIT_KEY_SECRET
import pandas as pd

import numpy as np

session = HTTP(
    testnet=False,
    api_key='eG0oUfh9Kc05PAZp55',
    api_secret='aGaVGQxhc6sEbTXfSOeBBLufs9gVu2qSBre5',
)


def get_kline_data(coin: str = "BTC") -> pd.DataFrame:
    symbol = coin + "USDT"
    kline_data = session.get_kline(
        category="linear",
        symbol=symbol,
        interval=15,
        limit=200
    )["result"]

    klines = np.array(kline_data['list'])
    df = pd.DataFrame(klines[:, [0, 1, 2, 3, 4, 5, 6]],
                      columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Turnover'])
    df.set_index('Time', inplace=True)

    # Transrofm values to numeric
    for col in ('Open', 'High', 'Low', 'Close', 'Volume', 'Turnover'):
        df[col] = df[col].astype(float)
    return df


def get_last_prices() -> tuple:
    """
    Функция для извлечения последней цены ETH и BTC.
    Для минимальной задержки можно использовать вебсокет, но в
    данной задаче нам будет достаточно http-соединения
    (а ещё это намного удобнее)
    """

    btc_close_price = session.get_kline(
        category="linear",
        symbol='BTCUSDT',
        interval=1,
        limit=1
    )["result"]['list'][0][4]
    eth_close_price = session.get_kline(
        category="linear",
        symbol='ETHUSDT',
        interval=1,
        limit=1
    )["result"]['list'][0][4]
    return float(btc_close_price), float(eth_close_price)

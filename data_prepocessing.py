import numpy as np
import pandas as pd
import ssl  # To may use unverified SSL
import matplotlib.pyplot as plt
from csv_extractor import get_historical_data
from ExchangeClient import get_kline_data  # актуальные данные с биржи

# Последние данные с биржи
eth_df = get_kline_data("ETH")
btc_df = get_kline_data()
btc_columns = ['High', 'Open', 'Close', 'Low', 'Volume', 'Turnover']


 # Исторические данные за несколько лет (второй вариант)
# eth_df = get_historical_data("ETH")
# btc_df = get_historical_data()
# btc_columns = ['High', 'Open', 'Close', 'Low', 'Volume BTC', 'Volume USDT', 'tradecount']

# Посмотрим на графики цен
fig, ax = plt.subplots(figsize=(15, 8))
btc_df[['High','Low']].plot(ax=ax,)
eth_df[['High','Low']].plot(ax=ax)
ax.legend(['BTC high', 'BTC low', "ETH high", "ETH low"])
plt.title('Максимальные и минимальные цены котировок')
plt.show()
#Видно, что Eth "следует" за BTC, однако оценить влияние BTC сложно






# Посмотрим на логарифмы цен
btc_df['LnClose'] = np.log(btc_df['Close'])
eth_df['LnClose'] = np.log(eth_df['Close'])
# Посмотрим, что получилось
eth_df.LnClose.plot()
btc_df.LnClose.plot()
plt.title('Цены после логарифмирования')
plt.show()
# Видим, что цены очень сильно коррелируют.


# Произведём z-масштабирование признаков (логарифмы здесь не
# нужны - результат будет тем же после стандартизации)
for df in (btc_df, eth_df):
    # for price_type in ('LnOpen', 'LnClose',"LnHigh", "LnLow"):
    for price_type in ('Open', 'Close', "High", "Low"):
        df[price_type] = (df[price_type] - df[price_type].mean()) / df[price_type].std()


eth_df.Close.plot()
btc_df.Close.plot()
plt.title('Цены после масштабирования')
plt.show()
# Теперь данные хорошо "ложатся" друг на друга, между графиками
# видна чёткая корреляция

import matplotlib.pyplot as plt
import statsmodels.api as sm
from data_prepocessing import btc_df, eth_df, btc_columns

# Рассчитаем коэффициент корреляции между ценами ETH и BTC
correlation = eth_df[['Close']].corrwith(btc_df['Close'], axis=0, numeric_only=True)
print('Correlation: ', correlation)


# Строим парную регрессионную модель
ols = sm.OLS(eth_df[['Close']], sm.add_constant(btc_df[btc_columns])).fit()

from statsmodels.iolib.summary2 import Summary
result: Summary = ols.summary()
print("Результат работы регрессионной модели:\n", result)

coint_t, pvalue, crit_value = sm.tsa.stattools.coint(btc_df[['Close']], eth_df[['Close']])
print(f'coint_t: {coint_t}\n'
      f'pvalue (вероятность соблюдения нулевой гипотезы): {pvalue}\n'
      f'crit_value (пределы статистически значимой коинтеграции: {crit_value}')

# Коэффициент влияния BTC на цену ETH
btc_impact_ratio = ols.params['Close']
print('Коэффициент влияния BTC на цену ETH: ', btc_impact_ratio)


# Определим собственные движения цены с помощью регрессии
model = sm.OLS(eth_df['Close'], sm.add_constant(btc_df[btc_columns] * btc_impact_ratio)).fit()
btc_impact_price = model.predict(sm.add_constant(btc_df[btc_columns] * btc_impact_ratio))
eth_df['IM'] = eth_df['Close'] - btc_impact_price  # Idiosyncratic Movements


# Покажем движение цены на графике
fig, ax = plt.subplots(figsize=(15, 8))
eth_df.Close.plot(ax=ax)
eth_df.IM.plot(ax=ax)
plt.plot(btc_impact_price)
plt.title('Собственное движение цены ETH на фоне абсолютного')
ax.legend(['Цена закрытия ETH', 'Собственные движения', "Движения вслед за BTC"])
plt.show()

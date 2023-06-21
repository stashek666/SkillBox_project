from time import sleep, time

from ExchangeClient import get_last_prices
from model import btc_impact_ratio

RANGE = 0.01  # 1%
PERIOD = 60 * 60  # 1 Hour


def send_notification(period, real_change, independent_change):
    print(
        f'Активное движение ETH за последние {period/60} минут!\n'
        f'Абсолютное изменение цены: {real_change}%\n'
        f'Собственное движение цены: {independent_change}%'
    )


class PriceHandler():
    def __init__(self):
        self.start_time = time()
        self.last_btc_price = None
        self.last_eth_price = None
        self.max = None
        self.min = None
        self.deviation = 0  # Отклонение от точки отсчёта
        self.true_deviation = 0

    def handle_prices(self, btc_price, eth_price):
        """
        Last price handling
        """

        if all((self.last_btc_price, self.last_eth_price)):
            # Изменения цены (в долларах)
            btc_delta = (btc_price - self.last_btc_price)
            eth_delta = (eth_price - self.last_eth_price)
            eth_IM_delta = eth_delta - btc_delta * btc_impact_ratio # Independent changes

            # Относительные изменения (дроби)
            eth_whole_change = eth_delta / self.last_eth_price
            eth_independent_change = eth_IM_delta / self.last_eth_price
            self.deviation += eth_whole_change  # Абсолютное движение
            self.true_deviation += eth_independent_change  # Независимое движение

            now = time()
            time_passed = now - self.start_time

            if time_passed > PERIOD or abs(self.deviation) > RANGE:

                if abs(self.deviation) > RANGE:
                    # Отправляем уведомление
                    send_notification(
                        PERIOD,
                        self.deviation * 100, self.true_deviation * 100
                    )

                # Сбрасываем время и отклонение цены
                self.start_time = now
                self.deviation = 0
                self.true_deviation = 0

        # else:
        #     pass
        self.last_btc_price = btc_price
        self.last_eth_price = eth_price


client = PriceHandler()


if __name__ == '__main__':
    print("\nОтслеживание цены запущено!")
    while True:
        sleep(3)
        btc_last_price, eth_last_price = get_last_prices()
        print('Время: ', time.ctime([сек]))
        print('Последняя цена ETH: ', eth_last_price)
        client.handle_prices(btc_last_price, eth_last_price)

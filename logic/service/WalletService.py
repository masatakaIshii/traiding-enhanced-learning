from datetime import date
from typing import Optional

from logic.FinanceService import FinanceService
from logic.Stock import Stock
from logic.Wallet import Wallet
from logic.exceptions.IncorrectBuyAmountError import IncorrectBuyAmountError
from logic.exceptions.StockNotFoundError import StockNotFoundError


class WalletService:
    def __init__(self, wallet: Wallet, finance_service: FinanceService):
        self.__wallet = wallet
        self.__finance_service = finance_service

    def get_amount(self):
        return self.__wallet.wallet_amount

    # amount is in dollar
    def buy_stock(self, cur_date_str: str, amount: float) -> Stock:
        stock_to_buy = self.__finance_service.get_stock(cur_date_str, amount)

        # TODO pourquoi multiplier par le share percentage ? on achète que le montant, le pourcentage est calculé après
        # stock_total_cost = stock_to_buy.purchase_value * (stock_to_buy.share_percentage / 100)

        if self.__wallet.wallet_amount - amount <= 0:
            raise IncorrectBuyAmountError
        self.__wallet.last_wallet_amount = self.__wallet.wallet_amount
        self.__wallet.wallet_amount -= amount
        self.__wallet.stocks.append(stock_to_buy)

        return stock_to_buy

    def get_stocks(self) -> [Stock]:
        return self.__wallet.stocks

    def get_stock(self, index: int) -> Optional[Stock]:
        stocks = self.__wallet.stocks
        if len(stocks) == index:
            return None
        return stocks[index]

    def sell_stock_and_return_profit(self, index: int, cur_date_str=date.today().strftime('%m-%d-%Y')):
        stocks = self.__wallet.stocks
        stock_to_sell: Stock = stocks.pop(index)

        cur_value = self.__finance_service.get_value_by_date(cur_date_str)
        if cur_value is None:
            raise StockNotFoundError
        # TODO chui pas certain là...
        cur_amount_value = cur_value * stock_to_sell.share_percentage / 100
        stock_to_sell_amount_value = stock_to_sell.purchase_value * stock_to_sell.share_percentage / 100
        profit: float = cur_amount_value - stock_to_sell_amount_value

        self.__wallet.last_wallet_amount = self.__wallet.wallet_amount
        self.__wallet.wallet_amount = self.__wallet.wallet_amount + cur_amount_value

        if profit > 0:
            bill_percent_on_profit = 0.3
            self.__wallet.wallet_amount -= profit * bill_percent_on_profit

            # profit -= profit * bill_percent_on_profit

        # return ((initial_value / self.__wallet.wallet_amount) - 1) * 100  # pour avoir le pourcentage

    @property
    def finance_service(self):
        return self.__finance_service

    def get_profit_percentage(self) -> float:
        # Formule du taux de variation
        if self.__wallet.wallet_amount == self.__wallet.initial_value:
            return 0
        return (self.__wallet.wallet_amount - self.__wallet.initial_value) / self.__wallet.initial_value * 100

    def can_buy_stock(self, amount: float) -> bool:
        return self.__wallet.wallet_amount > amount

    def can_sell_stock(self) -> bool:
        print(f"LEN STOCKS {len(self.__wallet.stocks)}")
        return len(self.__wallet.stocks) > 0

    def get_last_action_profit_percentage(self) -> float:
        # au lieu d'initial value on veut value - 1
        print(f"LAST WALLET AMOUNT {self.__wallet.last_wallet_amount}")
        print(f"WALLET AMOUNT {self.__wallet.wallet_amount}")
        if self.__wallet.wallet_amount == self.__wallet.last_wallet_amount:
            return 0
        return (self.__wallet.wallet_amount - self.__wallet.last_wallet_amount) / self.__wallet.last_wallet_amount * 100

    def keep_stock(self):
        self.__wallet.last_wallet_amount = self.__wallet.wallet_amount

    def reset(self):
        self.__wallet = Wallet()

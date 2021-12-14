# Récupérer les infos entre deux dates
# Sauvegarder le paquetol
# Faire les calculs au moment de l'achat / vente etc
from logic.FinanceService import FinanceService
from logic.exceptions.IncorrectBuyAmountError import IncorrectBuyAmountError


class Wallet:
    def __init__(self, wallet_amount=100):
        self.__wallet_amount = wallet_amount
        self.__stocks = []

    def buy(self, stock_name, amount):
        if amount > self.__wallet_amount:
            raise IncorrectBuyAmountError

        self.__wallet_amount -= amount

    @property
    def wallet_amount(self):
        return self.__wallet_amount

    @property
    def stocks(self):
        return self.__stocks

    def set_wallet_amount(self, amount):
        self.__wallet_amount = amount
